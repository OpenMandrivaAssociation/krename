Summary:	A powerful batch renamer for KDE
Name:		krename
Version:	5.0.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.krename.net/
Source0:	http://download.kde.org/stable/krename/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		krename-5.0.2-exiv2-0.28.patch
BuildRequires:	podofo-devel
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(Gettext)
BuildRequires:	cmake(PythonInterp)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5JS)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5)

%description
Krename is a very powerful batch file renamer for KF5 which can rename a list
of files based on a set of expressions. It can copy/move the files to another
directory or simply rename the input files.

Krename supports many conversion operations, including conversion of a filename
to lowercase or to uppercase, conversion of the first letter of every word to
uppercase, adding numbers to filenames, finding and replacing parts of the
filename, and many more. It can also change access and modification dates,
permissions, and file ownership.

%files -f %{name}.lang
%doc AUTHORS README.md
%{_kde5_bindir}/%{name}
%{_kde5_iconsdir}/*/*/apps/*.png
%{_kde5_services}/ServiceMenus/*.desktop
%{_datadir}/applications/org.kde.krename.desktop
%{_datadir}/metainfo/org.kde.krename.appdata.xml

#----------------------------------------------------------------------------

%prep
%autosetup -p1
for file in TODO; do
    iconv -f iso8859-1 -t utf8 $file > $file.utf8
    rm -rf $file
    mv $file.utf8 $file
done

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

%find_lang %{name} --with-html

