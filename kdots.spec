Name:           kdots
Version:        0.5.1
Release:        1%{?dist}
Summary:        The simple implementation of the game of dots

License:        BSD
URL:            https://projects.kde.org/projects/playground/games/kdots
Source0:        %{name}-%{version}.git.tar.xz

BuildRequires:  qt-devel
BuildRequires:  cmake
BuildRequires:  kdegames-devel
BuildRequires:  desktop-file-utils


%description
The purpose of Dots game is to catch your opponent's dots by placing your dots
on the game board where the lines cross.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{version}.git


%build
%cmake
make %{?_smp_mflags}


%install
%make_install
desktop-file-validate %{buildroot}%{_kde4_datadir}/applications/kde4/kdots.desktop

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc README.md COPYING AUTHORS
%{_bindir}/kdots
%{_libdir}/libkdotslib.so.*
%{_libdir}/kde4/kdots
%{_kde4_datadir}/applications/kde4/kdots.desktop
%{_datadir}/config.kcfg/kdots.kcfg
%{_kde4_datadir}/kde4/apps/kdots

%files devel
%doc
%{_libdir}/*.so


%changelog
* Wed Sep 19 2012 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.1-1.R
- Initial release