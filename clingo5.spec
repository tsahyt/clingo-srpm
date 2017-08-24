Name:    clingo5
Version: 5.2.1
Release: 2%{?dist}
Summary: The Potassco ASP suite executable, built from the Github repository

License: MIT
URL:     http://potassco.org
Source0: https://github.com/potassco/clingo/archive/v%{version}.tar.gz

BuildRequires: cmake, re2c, bison, python2-devel, python3-devel, lua-devel

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

%package -n python2-clingo5
Summary:    Potassco clingo python binding.
%description -n python2-clingo5
Python 2 bindings for the clingo C library.

%package -n python3-clingo5
Summary:    Potassco clingo python binding.
%description -n python3-clingo5
Python 3 bindings for the clingo C library.

%package -n lua-clingo5
Summary:    Potassco clingo lua binding.
%description -n lua-clingo5
Lua bindings for the clingo C library.

%prep
%autosetup -n clingo-%{version}

%build
cmake -H. -Brelease -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=%{__python3} -DCLINGO_MANAGE_RPATH=Off -DCMAKE_INSTALL_PREFIX=%{_prefix} -DPYCLINGO_USER_INSTALL=Off -DCLASP_BUILD_APP=Off -DLUACLINGO_INSTALL_DIR=%{lua_libdir}
cmake -H. -Bpython2 -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=%{__python2} -DCLINGO_MANAGE_RPATH=Off -DCMAKE_INSTALL_PREFIX=%{_prefix} -DPYCLINGO_USER_INSTALL=Off
cmake --build release -- -j8
cmake --build python2 --target pyclingo -- -j8

%install
make -Crelease DESTDIR=%{buildroot} install
make -Cpython2/app/pyclingo DESTDIR=%{buildroot} install
# NOTE: should the cmake configuration be made more flexible here?
test `basename %{_libdir}` = lib || mv %{buildroot}/%{_prefix}/lib/* %{buildroot}/%{_libdir}/

%files
%{_bindir}/clingo
%{_bindir}/gringo
%{_bindir}/reify

%files lib
%{_libdir}/libclingo.so
%{_libdir}/libclingo.so.*

%files lib-devel
%{_includedir}/clingo.h
%{_includedir}/clingo.hh

%files -n python2-clingo5
%{python2_sitearch}/clingo.*

%files -n python3-clingo5
%{python3_sitearch}/clingo.*

%files -n lua-clingo5
%{lua_libdir}/clingo.*

%changelog
* Tue Aug 22 2017 Paul Ogris <pogris@edu.aau.at> 5.2.1-1
- Changes submitted by Roland Kaminski
- Lua/Python packages
- Removed lpconvert
- Changed build process

* Fri Aug 18 2017 Paul Ogris <pogris@edu.aau.at> 5.2.1-1
- Update to clingo version 5.2.1

* Tue Oct 18 2016 Paul Ogris <pogris@edu.aau.at> 5.1.0-1
- Initial Packaging
