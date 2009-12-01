Name:           gnome-main-menu
License:        GPLv2+
Group:          Graphical desktop/GNOME
Version:        0.9.13
Release:        %mkrel 1
Summary:        The GNOME Desktop Menu
Source:         ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Patch0:		gnome-main-menu-0.9.13-nm-glib.patch
Url:            http://www.gnome.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gnome-common gnome-desktop-devel gnome-menus-devel gnome-panel-devel libnautilus-devel gtk-doc intltool libgnomeui2-devel dbus-glib-devel librsvg2-devel
BuildRequires:  eel-devel
BuildRequires:  libgtop2.0-devel hal-devel libiw-devel
BuildRequires:  libglade2.0-devel
BuildRequires:  scrollkeeper desktop-file-utils libnm-glib-devel
BuildRequires:	unique-devel libslab-devel
Obsoletes:	%{_lib}gnome-main-menu < 0.9.13
Requires:       gnome-panel dbus-glib hal tango-icon-theme gnome-system-monitor
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires(pre):  GConf2
Requires(post): GConf2
Requires(post): scrollkeeper
Requires(preun):  GConf2
Requires(postun): scrollkeeper

%description
The GNOME Desktop Menu and Application Browser.

%prep
%setup -q
%patch0 -p0

%build
autoreconf -fi
%configure2_5x \
  --disable-static \
  --disable-schemas-install \
  --enable-nautilus-extension

%make

%install
rm -fr %buildroot
%makeinstall_std
%find_lang %{name}

#autorun
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/gnome/autostart
cp application-browser/etc/application-browser.desktop $RPM_BUILD_ROOT/%{_datadir}/gnome/autostart/
sed -i "/^Exec=/ s/application-browser *$/application-browser -h/" $RPM_BUILD_ROOT/%{_datadir}/gnome/autostart/application-browser.desktop

%clean
rm -rf %buildroot

%define schemas slab application-browser

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

%files -f %{name}.lang
%defattr (-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/gnome-2.0/ui/GNOME_MainMenu_ContextMenu.xml
%{_datadir}/gnome/autostart/application-browser.desktop
%{_datadir}/applications/application-browser.desktop
%{_datadir}/applications/gnome-screensaver-lock.desktop
%{_datadir}/applications/gnome-session-logout.desktop
%{_datadir}/applications/gnome-session-shutdown.desktop
%{_datadir}/applications/trigger-panel-run-dialog.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_libdir}/bonobo/servers/GNOME_MainMenu.server
%{_libexecdir}/main-menu
%{_libdir}/nautilus/extensions-1.0/libnautilus-main-menu.*
