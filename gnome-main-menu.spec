%define name gnome-main-menu
%define version 0.6.3
%define major 0
%define libname %mklibname %{name}_ %major

Name:           %name 
License:        GPL
Group:          System/GUI/GNOME
Version:        0.6.3
Release:        %mkrel 1
Summary:        The GNOME Desktop Menu
Source:         %{name}-%{version}.tar.gz
Url:            http://www.gnome.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gnome-common gnome-desktop-devel gnome-menus-devel gnome-panel-devel gtk-doc intltool libgnomeui2-devel dbus-glib-devel librsvg2-devel
BuildRequires:  libgtop2.0-devel networkmanager-devel hal-devel libiw-devel
BuildRequires:  scrollkeeper desktop-file-utils
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

%description -n %{libname}
Libraries package for %{name}.

%package -n %{libname}-devel
Summary: Development package for %{name}
Group: Development/Other
Requires: %libname = %version
Provides: %libname-devel = %version-%release
Requires: %{name} = %{version} gtk2-devel libgnomeui2-devel libbonoboui2-devel libglade2.0-deve 
Requires: gnome-desktop-devel gnome-menus-devel glib2-devel pango-devel

%description -n %{libname}-devel
Development package for %{name}

%prep
%setup -q -n gnome-main-menu-%{version}

%build
%configure2_5x

%make

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
#make install DESTDIR=$RPM_BUILD_ROOT
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

%post
%post_install_gconf_schemas %{schemas}
%update_menus

%postun
%clean_menus

%preun
%preun_uninstall_gconf_schemas %{schemas}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -f %{name}.lang
%defattr (-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/gnome-2.0/ui/GNOME_MainMenu_ContextMenu.xml
%{_datadir}/gnome/autostart/application-browser.desktop
%lang(all) %{_datadir}/locale/*/LC_MESSAGES/*
%{_datadir}/applications/application-browser.desktop
%{_datadir}/applications/control-center.desktop
%{_datadir}/applications/main-menu-rug.desktop

%files -n %{libname}
%defattr (-, root, root)
%{_libdir}/*.so.%{major}*
%{_libdir}/bonobo/servers/GNOME_MainMenu.server
%{_libdir}/main-menu

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/lib*.a
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/lib*.la
%{_includedir}/*
%_libdir/pkgconfig/*


