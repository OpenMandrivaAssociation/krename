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
