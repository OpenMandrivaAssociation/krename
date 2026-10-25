%define git 20261017
%define commit 1149ef5b810084c9cc64e92d68235c6b67b88c09

Summary:	A powerful batch renamer for KDE
Name:		krename
Version:	5.0.60
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://invent.kde.org/utilities/krename
Source0:	https://invent.kde.org/utilities/krename/-/archive/%{commit}/krename-%{commit}.tar.bz2
Patch0:		krename-5.0.60-podofo-1.1.patch
Patch1:		krename-5.0.60-find-podofo.patch
BuildRequires:	pkgconfig(libpodofo)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Krename is a very powerful batch file renamer for KDE which can rename a list
of files based on a set of expressions. It can copy/move the files to another
directory or simply rename the input files.

Krename supports many conversion operations, including conversion of a filename
to lowercase or to uppercase, conversion of the first letter of every word to
uppercase, adding numbers to filenames, finding and replacing parts of the
filename, and many more. It can also change access and modification dates,
permissions, and file ownership.

%files -f %{name}.lang
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/applications/org.kde.krename.desktop
%{_datadir}/kio/servicemenus/*
%{_datadir}/metainfo/org.kde.krename.appdata.xml

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{commit}
