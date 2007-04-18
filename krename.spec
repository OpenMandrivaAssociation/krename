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
BuildRequires:  desktop-file-utils
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot


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

%setup -q -n%name-%{version}

%build
make -f admin/Makefile.common cvs

export QTDIR=%_prefix/%_lib/qt3
export KDEDIR=%_prefix

export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH
# Search for qt/kde libraries in the right directories (avoid patch)
# NOTE: please don't regenerate configure scripts below
perl -pi -e "s@/lib(\"|\b[^/])@/%_lib\1@g if /(kde|qt)_(libdirs|libraries)=/" configure

CFLAGS="%optflags" CXXFLAGS="%optflags" \
./configure	--prefix=%{_prefix} \
		--libdir=%{_libdir} \
		--mandir=%{_mandir} \
		--datadir=%{_datadir} \
		--disable-debug \
		--enable-mt \
		--enable-shared \
		--disable-static \
		--disable-objprelink \
		--with-pic \
		--with-gnu-ld \
		--disable-rpath \
		--disable-embedded \
		--enable-fast-install=yes \
		--with-xineramai\
		--enable-final
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-System-FileTools" \
  --add-category="System" \
  --add-category="FileManager" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications/kde $RPM_BUILD_ROOT%{_datadir}/applications/kde/*


install -m644 $RPM_BUILD_ROOT%{_iconsdir}/locolor/16x16/apps/%{name}.png -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%find_lang %{name}

%post
%update_menus
%if %mdkversion > 200600
%{update_desktop_database}
%update_icon_cache locolor
%update_icon_cache hicolor
%endif

%postun
%clean_menus
%if %mdkversion > 200600
%clean_icon_cache locolor
%clean_icon_cache hicolor
%endif

%clean
rm -rf $RPM_BUILD_ROOT

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
%{_datadir}/apps/konqueror/servicemenus/krename_dir.desktop
%{_datadir}/apps/konqueror/servicemenus/krenameservicemenu.desktop
