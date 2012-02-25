Summary:	The GNOME Desktop Menu
Name:		gnome-main-menu
Version:	0.9.15
Release:	2
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0:		gnome-main-menu-0.9.15-mandriva-integration.patch

BuildRequires:	desktop-file-utils
BuildRequires:  gnome-common
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libiw30-devel
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gnome-desktop-2.0)
#BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libgnome-menu)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(libnautilus-extension)
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libpanelapplet-2.0)
BuildRequires:	pkgconfig(libslab)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(unique-1.0)
#BuildRequires:	librsvg2-devel

Obsoletes:	%{_lib}gnome-main-menu < 0.9.15
Requires:	gnome-panel2
Requires:	dbus-glib
Requires:	tango-icon-theme
Requires:	gnome-system-monitor
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Requires(pre):  GConf2
Requires(post): GConf2
Requires(preun):  GConf2

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
rm -fr %{buildroot}
%makeinstall_std
%find_lang %{name}

#autorun
mkdir -p %{buildroot}/%{_datadir}/gnome/autostart
cp application-browser/etc/application-browser.desktop %{buildroot}/%{_datadir}/gnome/autostart/
sed -i "/^Exec=/ s/application-browser *$/application-browser -h/" %{buildroot}/%{_datadir}/gnome/autostart/application-browser.desktop

%files -f %{name}.lang
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

