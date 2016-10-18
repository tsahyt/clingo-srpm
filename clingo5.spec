Name:		clingo5
Version:	5.1.0
Release:	1%{?dist}
Summary:	The Potassco ASP suite executable, built from the Github repository

License:	GPLv3
URL:		http://potassco.org
Source0:    https://github.com/potassco/clingo/archive/v%{version}.tar.gz

BuildRequires: scons, re2c, bison

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
scons --build-dir=release
scons --build-dir=release libclingo

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_includedir}
mkdir -p %{buildroot}/%{_libdir}
install -p -m 755 build/release/clingo %{buildroot}/%{_bindir}
install -p -m 755 build/release/gringo %{buildroot}/%{_bindir}
install -p -m 755 build/release/reify %{buildroot}/%{_bindir}
install -p -m 755 build/release/lpconvert %{buildroot}/%{_bindir}
install -p -m 755 build/release/libclingo.so %{buildroot}/%{_libdir}
install -p -m 644 libgringo/clingo.h %{buildroot}/%{_includedir}

%files
%{_bindir}/clingo
%{_bindir}/gringo
%{_bindir}/reify
%{_bindir}/lpconvert

%files lib
%{_libdir}/libclingo.so

%files lib-devel
%{_includedir}/clingo.h

%changelog
* Tue Oct 18 2016 Paul Ogris <pogris@edu.aau.at> 5.1.0-1
- Initial Packaging
