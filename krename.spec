Summary:	A powerful batch renamer for KDE
Name:		krename
Version:	4.0.9
Release:	%mkrel 2
Summary:	A powerful batch renamer for KDE
License:	GPLv2+
Url:		http://www.krename.net/
Group:		Graphical desktop/KDE
Source0: 	http://downloads.sourceforge.net/krename/%{name}-%{version}.tar.bz2
Patch0:		krename-4.0.9-rus.patch
Patch1:		krename-4.0.9-desktop-rus.patch
Patch2:		krename-4.0.9-podofo.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	podofo-devel
BuildRequires:	taglib-devel
BuildRequires:	pkgconfig(exiv2)

%description
Krename is a very powerful batch file renamer for KDE4
which can rename a list of files based on a set of expressions.
It can copy/move the files to another directory or simply
rename the input files.
prename supports many conversion operations, including
conversion of a filename to lowercase or to uppercase,
conversion of the first letter of every word to uppercase,
adding numbers to filenames, finding and replacing parts of
the filename, and many more. It can also change access and
modification dates, permissions, and file ownership.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
for file in TODO; do
    iconv -f iso8859-1 -t utf8 $file > $file.utf8
    rm -rf $file
    mv $file.utf8 $file
done

%build
%cmake_kde4
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%find_lang %{name} --with-html

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%doc AUTHORS README
%{_kde_bindir}/%{name}
%{_kde_services}/ServiceMenus/*.desktop
%{_kde_applicationsdir}/*.desktop
%{_kde_iconsdir}/*/*/apps/*.png


%changelog
* Wed May 02 2012 Andrey Bondrov <abondrov@mandriva.org> 4.0.9-2mdv2012.0
+ Revision: 795039
- Build PDF plugin (with PoDoFo lib), add patches with russian translation

* Tue Feb 14 2012 Andrey Bondrov <abondrov@mandriva.org> 4.0.9-1
+ Revision: 774042
- New version 4.0.9

* Sat May 21 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.0.7-2
+ Revision: 676463
- Add fedora patch to correct crash in static initializer
  CCBUG: 63233

* Mon May 09 2011 Funda Wang <fwang@mandriva.org> 4.0.7-1
+ Revision: 672674
- update to new version 4.0.7

* Sun Jan 30 2011 Funda Wang <fwang@mandriva.org> 4.0.6-1
+ Revision: 634123
- new version 4.0.6

* Wed Dec 01 2010 Funda Wang <fwang@mandriva.org> 4.0.5-2mdv2011.0
+ Revision: 604400
- rebuild for new exiv2

* Thu Nov 18 2010 Funda Wang <fwang@mandriva.org> 4.0.5-1mdv2011.0
+ Revision: 598556
- update to new version 4.0.5

* Tue Aug 03 2010 Funda Wang <fwang@mandriva.org> 4.0.4-2mdv2011.0
+ Revision: 565555
- rebuild for new exiv2

* Sat Jul 17 2010 Funda Wang <fwang@mandriva.org> 4.0.4-1mdv2011.0
+ Revision: 554501
- update to new version 4.0.4

* Thu Dec 31 2009 Funda Wang <fwang@mandriva.org> 4.0.3-2mdv2010.1
+ Revision: 484308
- rebuild for new exiv

* Mon Dec 28 2009 Frederik Himpe <fhimpe@mandriva.org> 4.0.3-1mdv2010.1
+ Revision: 482916
- update to new version 4.0.3

* Sat Dec 05 2009 Funda Wang <fwang@mandriva.org> 4.0.2-1mdv2010.1
+ Revision: 473663
- new version 4.0.2

* Thu Nov 12 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 4.0.1-2mdv2010.1
+ Revision: 465245
- Rebuild against new Qt

* Mon Nov 09 2009 Funda Wang <fwang@mandriva.org> 4.0.1-1mdv2010.1
+ Revision: 463298
- update to new version 4.0.1

* Thu Sep 24 2009 Frederik Himpe <fhimpe@mandriva.org> 4.0.0-1mdv2010.0
+ Revision: 448401
- Fix build on x86_64 by disabling parallel build

  + Funda Wang <fwang@mandriva.org>
    - New version 4.0.0

* Tue Jun 02 2009 Funda Wang <fwang@mandriva.org> 3.9.3-1mdv2010.0
+ Revision: 382128
- BR exiv
- New version 3.9.3

* Wed May 13 2009 Funda Wang <fwang@mandriva.org> 3.9.2-2mdv2010.0
+ Revision: 375220
- add svn patch fix services

* Sat Oct 11 2008 Funda Wang <fwang@mandriva.org> 3.9.2-1mdv2009.1
+ Revision: 291877
- New version 3.9.2

* Sun Jul 06 2008 Funda Wang <fwang@mandriva.org> 3.9.1-1mdv2009.0
+ Revision: 232239
- New version 3.9.1 (kde4 version)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Per Ã˜yvind Karlsen <peroyvind@mandriva.org>
    - more proper fix for qt3 lib path
    - use %%configure2_5x macro

* Thu Apr 19 2007 Anssi Hannula <anssi@mandriva.org> 1mdv2008.0-current
+ Revision: 14960
- remove lib64 build hack (fixes build on lib64)
- do not wrongly override QTDIR (fixes build)

  + Nicolas LÃ©cureuil <nlecureuil@mandriva.com>
    - New version 3.0.14
    - Kill all debian menu style
    - Import krename



* Sun Jul 02 2006 Nicolas Lécureuil <neoclust@mandriva.org> 3.0.11-3mdv2007.0
- Rebuild for new extension and menu
- Use macros for icons

* Fri May 19 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 3.0.11-2mdk
- build with automake1.8

* Tue Mar 21 2006 Nicolas Lécureuil <neoclust@mandriva.org> 3.0.11-1mdk
- New release 3.0.11

* Thu Jan 12 2006 Laurent MONTEL <lmontel@mandriva.com> 3.0.10-1
- 3.0.10

* Mon Dec 26 2005 Nicolas Lécureuil <neoclust@mandriva.org> 3.0.9-2mdk
- Fix Buildrequires
- Fix Build
- Remove redundant buildrequires

* Wed Oct 19 2005 Lenny Cartier <lenny@mandriva.com> 3.0.9-1mdk
- 3.0.9

* Mon Sep 26 2005 Nicolas Lécureuil <neoclust@mandriva.org> 3.0.8-1mdk
- New release 3.0.8
- Fix some redundant BuildRequires

* Fri Jul 08 2005 Laurent MONTEL <lmontel@mandriva.com> 3.0.6-2
- Rebuild 

* Tue Jun 21 2005 Lenny Cartier <lenny@mandriva.com> 3.0.6-1mdk
- 3.0.6

* Mon May 23 2005 Sebastien Savarin <plouf@mandriva.org> 3.0.5-2mdk
- Suppression of the ugly patch

* Mon May 23 2005 Sebastien Savarin <plouf@mandriva.org> 3.0.5-1mdk
- New Release 3.0.5
- Fix build on amd64
- Use %%mkrel

* Thu Apr 21 2005 Laurent MONTEL <lmontel@mandriva.com> 3.0.4-1mdk
- 3.0.4

* Mon Feb 14 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0.3-1mdk
- 3.0.3

* Tue Jan 25 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0.3-0.rc2.2mdk
- Add patch1: don't rename device (it's not autorize)

* Fri Jan 07 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0.3-0.rc2.1mdk
- rc2

* Wed Dec 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0.3-0.rc1.1mdk
- 3.0.3rc1

* Mon Aug 09 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.0.2-1mdk
- 3.0.2

* Thu Jul 22 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0.1-1mdk
- 3.0.1

* Wed Jun 30 2004  Lenny Cartier <lenny@mandrakesoft.com> 3.0.0-1mdk
- 3.0.0

* Fri Jun 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0.0-0.rc1.2mdk
- REbuild

* Tue May 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0.0-0.rc1.1mdk
- 3.0.0rc1

* Wed Apr 21 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 2.9.4-1mdk
- 2.9.4

* Wed Jan 14 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.8.5-1mdk
- really update to 2.8.5
- fix changelog

* Thu Jan 08 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.8.5-1mdk
- 2.8.5

* Fri Dec 12 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.8.4-1mdk
- 2.8.4
- fix buildrequires (lib64..)
- --enable-final

* Thu Oct 23 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.8.3-2mdk
- fix hardcoded path

* Tue Oct 21 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.8.3-1mdk
- 2.8.3

* Wed Aug 06 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.8.2-1mdk
- 2.8.2

* Sun Jul 27 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.8.1-1mdk
- 2.8.1
- commented out --enable-final, won't compile for now

* Fri Jun 20 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.6.2-2mdk
- update url
- fix path to qt3 (lib64 issues..)
- --with-xinerama

* Sun May 11 2003 Laurent Culioli <laurent@pschit.net> 2.6.2-1mdk
- 2.6.2

* Tue Apr 01 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.5.5-1mdk
- 2.5.5

* Mon Mar 17 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.5.4-2mdk
- fix buildrequires

* Fri Mar 14 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.5.4-1mdk
- 2.5.4
- added some docs

* Fri Mar 14 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.5.3-3mdk
- hot dangedydang, even more missing BuildRequires

* Tue Mar 11 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 2.5.3-2mdk
- add missing BuildRequires
- .spec cleanups

* Sun Feb 16 2003 Laurent Culioli <laurent@pschit.net> 2.5.3-1mdk
- 2.5.3

* Wed Feb 12 2003 Laurent Culioli <laurent@pschit.net> 2.5.1-1mdk
- 2.5.1
- drop patch0 & 1

* Sat Feb 01 2003 Lenny Cartier <lenny@mandrakesoft.com 2.4.1-2mdk
- rebuild

* Tue Nov 12 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.4.1-1mdk
- from Per Øyvind Karlsen <peroyvind@delonic.no> :
	- 2.4.1
	- Patch #0 updated
	- Fixed deprecated headers with Patch #1

* Mon Oct 21 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.4-1mdk
- from Per Øyvind Karlsen <peroyvind@delonic.no> :
	- Initial release
