Summary: InfiniBand fabric simulator for management
Name: ibsim
Version: 0.5
Release: 4%{?dist}
License: GPLv2 or BSD
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source: http://www.openfabrics.org/downloads/%{name}/%{name}-%{version}-0.1.g327c3d8.tar.gz
Url: http://openfabrics.org/
BuildRequires: libibmad-devel
Conflicts: openib-diags < 1.3
ExclusiveArch: i386 x86_64 ia64 ppc ppc64
%description
ibsim provides simulation of infiniband fabric for using with OFA OpenSM,
diagnostic and management tools. 

%prep
%setup -q

%build
export CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}} -fno-strict-aliasing"
export LDFLAGS="${LDFLAGS:-${RPM_OPT_FLAGS}}"
make prefix=%_prefix libpath=%_libdir binpath=%_bindir %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
export CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}} -fno-strict-aliasing"
export LDFLAGS="${LDFLAGS:-${RPM_OPT_FLAGS}}"
make DESTDIR=${RPM_BUILD_ROOT} prefix=%_prefix libpath=%_libdir binpath=%_bindir install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_libdir}/umad2sim/libumad2sim*.so*
%{_bindir}/ibsim
%doc README COPYING TODO net-examples scripts

%changelog
* Fri Mar 12 2010 Doug Ledford <dledford@redhat.com> - 0.5-4.el6
- Rebuild against latest opensm, which was required for latest ibutils,
  which was required to resolve licensing issues during pkgwrangler review
- Related: bz555835

* Mon Jan 25 2010 Doug Ledford <dledford@redhat.com> - 0.5-3.el6
- Cleanups for pkgwrangler import
- Related: bz543948

* Tue Dec 22 2009 Doug Ledford <dledford@redhat.com> - 0.5-2.el5
- Update to latest upstream version
- Related: bz518218

* Fri Apr 17 2009 Doug Ledford <dledford@redhat.com> - 0.5-1.el5
- Update to ofed 1.4.1-rc3 version
- Related: bz459652

* Wed Sep 17 2008 Doug Ledford <dledford@redhat.com> - 0.4-3
- Rebuild against updated libibmad and libibumad libraries
- Only need to build require libibmad, it pulls in libibumad
- Resolves: bz451466

* Sun Jan 27 2008 Doug Ledford <dledford@redhat.com> - 0.4-2
- Add a conflicts against the old openib-diags package

* Fri Jan 25 2008 Doug Ledford <dledford@redhat.com> - 0.4-1
- Initial import into CVS
- Related: bz428197

