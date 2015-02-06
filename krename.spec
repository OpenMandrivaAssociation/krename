Summary:	A powerful batch renamer for KDE
Name:		krename
Version:	4.0.9
Release:	4
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.krename.net/
Source0:	http://downloads.sourceforge.net/krename/%{name}-%{version}.tar.bz2
Patch0:		krename-4.0.9-rus.patch
Patch1:		krename-4.0.9-desktop-rus.patch
Patch2:		krename-4.0.9-podofo.patch
Patch3:		krename-4.0.9-cmake.patch
Patch4:		krename-4.0.9-includedir.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	podofo-devel
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(freetype2)

%description
Krename is a very powerful batch file renamer for KDE4 which can rename a list
of files based on a set of expressions. It can copy/move the files to another
directory or simply rename the input files.

Krename supports many conversion operations, including conversion of a filename
to lowercase or to uppercase, conversion of the first letter of every word to
uppercase, adding numbers to filenames, finding and replacing parts of the
filename, and many more. It can also change access and modification dates,
permissions, and file ownership.

%files -f %{name}.lang
%doc AUTHORS README
%{_kde_bindir}/%{name}
%{_kde_services}/ServiceMenus/*.desktop
%{_kde_applicationsdir}/*.desktop
%{_kde_iconsdir}/*/*/apps/*.png

#----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches
for file in TODO; do
    iconv -f iso8859-1 -t utf8 $file > $file.utf8
    rm -rf $file
    mv $file.utf8 $file
done

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html

