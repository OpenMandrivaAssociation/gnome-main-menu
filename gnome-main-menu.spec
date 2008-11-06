%define name gnome-main-menu
%define version 0.9.10
%define svn 0
%define rel 3
%if %svn
%define release %mkrel -c %svn %rel
%else
%define release %mkrel %rel
%endif

%define libname %mklibname %{name}
%define develname %mklibname -d %{name}
#Legacy name (obsolete)
%define obslibname %mklibname %{name}_ 0


Name:           %name 
License:        GPLv2+
Group:          Graphical desktop/GNOME
Version:        %version
Release:        %release
Summary:        The GNOME Desktop Menu
%if %svn
Source:         %{name}-%{version}-%{svn}.tar.bz2
%else
Source:         %{name}-%{version}.tar.bz2
%endif
Url:            http://www.gnome.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gnome-common gnome-desktop-devel gnome-menus-devel gnome-panel-devel libnautilus-devel gtk-doc intltool libgnomeui2-devel dbus-glib-devel librsvg2-devel
BuildRequires:  libgtop2.0-devel hal-devel libiw-devel
BuildRequires:  scrollkeeper desktop-file-utils libnm_glib-devel
Requires:       gnome-panel dbus-glib hal tango-icon-theme gnome-system-monitor
Requires:	%{libname} = %{version}

Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires(pre):  GConf2
Requires(post): GConf2
Requires(post): scrollkeeper
Requires(preun):  GConf2
Requires(postun): scrollkeeper

%description
The GNOME Desktop Menu and Application Browser.

%package -n %{libname}
Summary: Libraries package for %{name}
Group: System/Libraries
Obsoletes: %{obslibname}

%description -n %{libname}
Libraries package for %{name}.

%package -n %{develname}
Summary: Development package for %{name}
Group: Development/Other
Requires: %libname = %version

%description -n %{develname}
This package contains development files for %{name}.

%prep
%setup -q

%build
sed -i s/^ENABLE_DYNAMIC_LIBSLAB=1/ENABLE_DYNAMIC_LIBSLAB=0/ configure.in
%configure2_5x \
  --enable-nautilus-extension

%make

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall_std
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL
%find_lang %{name}

#autorun
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/gnome/autostart
cp application-browser/etc/application-browser.desktop $RPM_BUILD_ROOT/%{_datadir}/gnome/autostart/
sed -i "/^Exec=/ s/application-browser *$/application-browser -h/" $RPM_BUILD_ROOT/%{_datadir}/gnome/autostart/application-browser.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%define schemas slab control-center application-browser

%if %mdkversion < 200900
%post
%post_install_gconf_schemas %{schemas}
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%preun
%preun_uninstall_gconf_schemas %{schemas}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -f %{name}.lang
%defattr (-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/gnome-2.0/ui/GNOME_MainMenu_ContextMenu.xml
%{_datadir}/gnome/autostart/application-browser.desktop
%{_datadir}/applications/application-browser.desktop
%{_datadir}/applications/gnome-screensaver-lock.desktop
%{_datadir}/applications/gnome-session-kill.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%files -n %{libname}
%defattr (-, root, root)
%{_libdir}/bonobo/servers/GNOME_MainMenu.server
%{_libdir}/main-menu
%{_libdir}/nautilus/extensions-1.0/libnautilus-main-menu.*
%{_libdir}/*.so.0*

%files -n %{develname}
%defattr (-, root, root)
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_includedir}/slab
%{_libdir}/pkgconfig/*.pc
