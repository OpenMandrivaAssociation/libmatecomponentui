%define api	2
%define major	0
%define libname	%mklibname matecomponentui %{api} %{major}
%define devname	%mklibname -d matecomponentui

Summary:	Library for compound documents in MATE
Name:		libmatecomponentui
Version:	1.4.0
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		System/Libraries
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libmate-2.0)
BuildRequires:	pkgconfig(libmatecanvas-2.0)
BuildRequires:	pkgconfig(libmatecomponent-2.0)

%description
Matecomponentui is a library that provides the necessary framework for MATE
applications to deal with compound documents, i.e. those with a
spreadsheet and graphic embedded in a word-processing document.

This package contains various needed modules and files for MATE
to operate.

%package -n %{libname}
Summary:	Library for compound documents in MATE
Group:		%{group}

%description -n %{libname}
This package provides library for %{name}.


%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static \

%make

%install
%makeinstall_std

%{find_lang} %{name}

%files -f %{name}.lang
%doc README NEWS changes.txt
%{_bindir}/*
%{_libdir}/matecomponent/servers/*
%{_libdir}/matecomponent-2.0
%{_libdir}/libglade/2.0/*.so
%{_datadir}/mate-2.0
%{_datadir}/applications/matecomponent-browser.desktop

%files -n %{libname}
%{_libdir}/libmatecomponentui-%{api}.so.%{major}*

%files -n %{devname}
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

