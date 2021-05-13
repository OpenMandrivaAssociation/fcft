%define libname %mklibname %{name}_ %{major}
%define devname %mklibname -d %{name}

%define major 3

Name:           fcft
Version:        2.4.0
Release:        1
Summary:        Simple library for font loading and glyph rasterization

License:        MIT and Unicode
URL:            https://codeberg.org/dnkl/fcft
Source0:        https://codeberg.org/dnkl/fcft/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson

BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(tllist)
# require *-static for header-only library
BuildRequires:  tllist-static

%description
fcft is a small font loading and glyph rasterization library built
on top of FontConfig, FreeType2 and pixman.
It can load and cache fonts from a fontconfig-formatted name string,
e.g. Monospace:size=12, optionally with user configured fallback fonts.

%package -n %{libname}
Summary:	Libraries for fcft
Group:		System/Libraries

%description -n %{libname}
This package provides the shared fcft library.


%package -n %{devname}
Summary:        Development files for %{name}
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}
cp unicode/LICENSE LICENSE.Unicode

%build
%meson
%meson_build

%install
%meson_install
# license will be installed to the correct location with rpm macros
rm -f %{buildroot}%{_docdir}/%{name}/LICENSE


%files
%license LICENSE LICENSE.Unicode
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/CHANGELOG.md
%{_docdir}/%{name}/README.md

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/%{name}*.3*
