%define name	krename
%define version	3.0.14
%define release %mkrel 1

Summary:	A powerful batch renamer for KDE
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Url:		http://www.krename.net/
Group:		Graphical desktop/KDE
Source0: 	http://prdownloads.sourceforge.net/krename/%{name}-%{version}.tar.bz2

BuildRequires:  kdelibs-devel 
BuildRequires:  mandriva-create-kde-mdk-menu


%description
Krename is a very powerful batch file renamer for KDE3
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
make -f admin/Makefile.common cvs

export QTDIR=%{_prefix}/lib/qt3/%{_lib}

%configure2_5x	--enable-final \
		--disable-rpath
%make

%install
rm -rf %{buildroot}
%{makeinstall_std}

install -m644 %{buildroot}%{_iconsdir}/locolor/16x16/apps/%{name}.png -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png -D %{buildroot}%{_liconsdir}/%{name}.png

%find_lang %{name}

%post
%if %mdkversion > 200600
%{update_desktop_database}
%update_icon_cache locolor
%update_icon_cache hicolor
%endif

%postun
%if %mdkversion > 200600
%clean_icon_cache locolor
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang 
%defattr(-,root,root)
%doc %{_docdir}/HTML/*/%{name}
%doc AUTHORS ChangeLog INSTALL README
%{_bindir}/%{name}
%{_datadir}/applications/kde/krename.desktop
%{_datadir}/apps/%{name}
%{_iconsdir}/locolor/16x16/apps/%{name}.png
%{_iconsdir}/locolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/apps/konqueror/servicemenus/*
