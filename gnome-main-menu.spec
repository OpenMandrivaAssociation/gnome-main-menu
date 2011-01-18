Name:           gnome-main-menu
License:        GPLv2+
Group:          Graphical desktop/GNOME
Version:        0.9.15
Release:        %mkrel 1
Summary:        The GNOME Desktop Menu
Source:         ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Patch0:		gnome-main-menu-0.9.15-mandriva-integration.patch
Url:            http://www.gnome.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gnome-common
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-menus-devel
BuildRequires:	gnome-panel-devel
BuildRequires:	libnautilus-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	dbus-glib-devel
BuildRequires:	librsvg2-devel
# BuildRequires:  eel-devel
BuildRequires:  libgtop2.0-devel
BuildRequires:	hal-devel
BuildRequires:	libiw-devel
BuildRequires:  libglade2.0-devel
BuildRequires:  scrollkeeper
BuildRequires:	desktop-file-utils
BuildRequires:	libnm-glib-devel
BuildRequires:	unique-devel
BuildRequires:	libslab-devel
BuildRequires:	libsm-devel
Obsoletes:	%{_lib}gnome-main-menu < 0.9.15
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
%patch0 -p1

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
%{_libdir}/nautilus/extensions-2.0/libnautilus-main-menu.*
