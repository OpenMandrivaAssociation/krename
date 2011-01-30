%define name	krename
%define version	4.0.6
%define release %mkrel 1

Summary:	A powerful batch renamer for KDE
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Url:		http://www.krename.net/
Group:		Graphical desktop/KDE
Source0: 	http://downloads.sourceforge.net/krename/%{name}-%{version}.tar.bz2
BuildRequires:  kdelibs4-devel
BuildRequires:	taglib-devel
BuildRequires:	libexiv-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang %{name} --with-html

%clean
rm -rf %{buildroot}

%files -f %{name}.lang 
%defattr(-,root,root)
%doc AUTHORS README
%{_kde_bindir}/%{name}
%{_kde_services}/ServiceMenus/*.desktop
%{_kde_applicationsdir}/*.desktop
%{_kde_iconsdir}/*/*/apps/*.png
