Name:		clingo5
Version:	5.2.1
Release:	2%{?dist}
Summary:	The Potassco ASP suite executable, built from the Github repository

License:	MIT
URL:		http://potassco.org
Source0:    https://github.com/potassco/clingo/archive/v%{version}.tar.gz

BuildRequires: cmake, re2c, bison, python3-devel, lua-devel

%description
Gringo is a grounder that, given an input program with first-order variables,
computes an equivalent ground (variable-free) program. Its output can be
processed further with answer set solver clasp. Starting with gringo series 5,
its output is no longer compatible with solvers like smodels or cmodels
reading smodels format.

Clingo combines both gringo and clasp into a monolithic system. This way it
offers more control over the grounding and solving process than gringo and
clasp can offer individually.

%package lib
Summary:    Potassco clingo library.
%description lib
Clingo library for use of the solver outside of standalone applications

%package lib-devel
Summary:    Potassco clingo library.
Requires:   %{name}-lib = %{version}-%{release}
%description lib-devel
Clingo library for use of the solver outside of standalone applications

%prep
%autosetup -n clingo-%{version}

%build
cmake -H. -Brelease -DCMAKE_BUILD_TYPE=Release
cmake --build release

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_includedir}
mkdir -p %{buildroot}/%{_libdir}
install -p -m 755 release/bin/clingo %{buildroot}/%{_bindir}
install -p -m 755 release/bin/gringo %{buildroot}/%{_bindir}
install -p -m 755 release/bin/reify %{buildroot}/%{_bindir}
install -p -m 755 release/bin/lpconvert %{buildroot}/%{_bindir}
install -p -m 755 release/bin/libclingo.so %{buildroot}/%{_libdir}
install -p -m 755 release/bin/libclingo.so.1 %{buildroot}/%{_libdir}
install -p -m 755 release/bin/libclingo.so.1.0 %{buildroot}/%{_libdir}
install -p -m 644 libclingo/clingo.h %{buildroot}/%{_includedir}

%files
%{_bindir}/clingo
%{_bindir}/gringo
%{_bindir}/reify
%{_bindir}/lpconvert

%files lib
%{_libdir}/libclingo.so
%{_libdir}/libclingo.so.1
%{_libdir}/libclingo.so.1.0

%files lib-devel
%{_includedir}/clingo.h

%changelog
* Tue Aug 18 2017 Paul Ogris <pogris@edu.aau.at> 5.2.1-2
- Fix changed license

* Tue Aug 18 2017 Paul Ogris <pogris@edu.aau.at> 5.2.1-1
- Update to clingo version 5.2.1

* Fri Oct 18 2016 Paul Ogris <pogris@edu.aau.at> 5.1.0-1
- Initial Packaging
