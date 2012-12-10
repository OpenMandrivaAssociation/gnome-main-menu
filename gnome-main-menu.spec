Summary:	The GNOME Desktop Menu
Name:		gnome-main-menu
Version:	0.9.16
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch1:		gnome-main-menu-0.9.15_glib_h.patch

BuildRequires:	desktop-file-utils
BuildRequires:  gnome-common
BuildRequires:	gtk-doc
BuildRequires:	intltool
#BuildRequires:	libiw-devel
#BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(gnome-desktop-2.0)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(libnautilus-extension)
BuildRequires:	pkgconfig(libpanelapplet-2.0)
BuildRequires:	pkgconfig(libslab)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(unique-1.0)

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
%apply_patches

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
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
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
%{_libdir}/nautilus/extensions-3.0/libnautilus-main-menu.*



%changelog
* Sun Feb 26 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.9.16-1
+ Revision: 780823
- new version 0.9.16
- p0 upstreamed
- removed unnecessary BRs
- disabled iw and nm build (no longer supported)
- added p1 to fix glib.h build failure
- rebuild
- cleaned up spec

* Tue Jan 18 2011 Alexandre Lissy <alissy@mandriva.com> 0.9.15-1
+ Revision: 631621
- * Adding BuildRequires against libsm-devel
- * Update to 0.9.15 release
 * Better mandriva integration (draknet/network manager, etc.)

  + Götz Waschk <waschk@mandriva.org>
    - rebuild for new libgnome-desktop

* Tue Dec 01 2009 Funda Wang <fwang@mandriva.org> 0.9.13-1mdv2010.1
+ Revision: 472176
- new version 0.9.13

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Mar 14 2009 Emmanuel Andry <eandry@mandriva.org> 0.9.12-2mdv2009.1
+ Revision: 355134
- rebuild

* Tue Jan 06 2009 Götz Waschk <waschk@mandriva.org> 0.9.12-1mdv2009.1
+ Revision: 326210
- update build deps
- new version
- fix build
- update file list

* Thu Nov 06 2008 Götz Waschk <waschk@mandriva.org> 0.9.10-3mdv2009.1
+ Revision: 300206
- rebuild for new  gnome-desktop

* Wed Jul 23 2008 Götz Waschk <waschk@mandriva.org> 0.9.10-2mdv2009.0
+ Revision: 242327
- fix build deps
- update license

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun May 25 2008 Funda Wang <fwang@mandriva.org> 0.9.10-1mdv2009.0
+ Revision: 211111
- BR networkmanager-glib
- New version 0.9.10

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 29 2007 Emmanuel Andry <eandry@mandriva.org> 0.9.8-0.258.3mdv2008.0
+ Revision: 93923
- rebuild for latest libiw (bug #33978)

* Thu Jun 21 2007 Funda Wang <fwang@mandriva.org> 0.9.8-0.258.2mdv2008.0
+ Revision: 42281
- fix rpm group

* Tue Apr 17 2007 Colin Guthrie <cguthrie@mandriva.org> 0.9.8-0.258.1mdv2008.0
+ Revision: 13644
- Update to 0.9.8 (svn258)
- Compile libslab statically until gnome-control-center is updated


* Fri Mar 09 2007 Jérôme Soyer <saispo@mandriva.org> 0.6.3-1mdv2007.1
+ Revision: 138723
- Add BR
- Add BR
- Add BR
- Import gnome-main-menu

