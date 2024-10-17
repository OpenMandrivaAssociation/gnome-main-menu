%define url_ver    %(echo %{version}|cut -d. -f1,2)
%define oname mate-main-menu

Summary:	Menu and Application Browser for MATE Desktop
Name:		gnome-main-menu
Version:	1.8.0
Release:	3
License:	GPLv2+
Url:		https://mate-desktop.org
Group:		Graphical desktop/GNOME
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		gnome-main-menu-1.8.0_format-not-a-literal-string.patch
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	libiw-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnm-glib-vpn)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(libcaja-extension)
BuildRequires:	pkgconfig(libmatepanelapplet-4.0)
BuildRequires:	pkgconfig(libslab)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(unique-1.0)
Requires:	dbus-glib
Requires:	tango-icon-theme
Requires:	mate-control-center
Requires:	mate-panel
%rename	%{oname}

%description
The MATE Desktop Menu and Application Browser.

%prep
%setup -q
%autopatch -p1

%build
%configure \
	--enable-caja-extension

%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
%{_libexecdir}/main-menu
%{_libdir}/caja/extensions-2.0/libcaja-main-menu.so
%{_datadir}/applications/*.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/dbus-1/services/org.mate.panel.applet.GNOMEMainMenuFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.gnome-main-menu.application-browser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.gnome-main-menu.gschema.xml
%{_datadir}/mate-control-center/applications.xbel
%{_datadir}/mate-control-center/documents.xbel
%{_datadir}/mate-control-center/empty.ots
%{_datadir}/mate-control-center/empty.ott
%{_datadir}/mate-control-center/places.xbel
%{_datadir}/mate-control-center/system-items.xbel
%{_datadir}/mate-panel/applets/org.mate.GNOMEMainMenu.mate-panel-applet
%{_mandir}/man1/application-browser.1*

