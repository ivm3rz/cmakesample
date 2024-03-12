Name:      cmakesample
Summary:   CMake-based AuroraOS application
Version:   0.1
Release:   1
License:   BSD-3-Clause
Source0:   %{name}-%{version}.tar.bz2
Requires:  sailfishsilica-qt5 >= 0.10.9
BuildRequires: cmake

%description
This sample project shows how to build a Aurora application with a custom build system.

%prep
%autosetup

%build
%cmake
%make_build

%install
%make_install

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%defattr(644,root,root,-)
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
