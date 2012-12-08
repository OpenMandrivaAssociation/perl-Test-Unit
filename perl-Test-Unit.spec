%define upstream_name    Test-Unit
%define upstream_version 0.25

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Error\\)'
%else
%define _requires_exceptions perl(Error)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Test::Unit::TestCase - unit testing framework base class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Test::Unit::TestCase is the 'workhorse' of the PerlUnit framework.
When writing tests, you generally subclass Test::Unit::TestCase,
write set_up and tear_down functions if you need them, a bunch of
test_* test methods, then do

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

# perl path hack
find . -type f | xargs perl -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog Changes README doc examples
%{perl_vendorlib}/Test/*.p*
%{perl_vendorlib}/Test/Unit
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.250.0-5mdv2012.0
+ Revision: 765752
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.250.0-4
+ Revision: 764257
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.250.0-3
+ Revision: 667392
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.250.0-2mdv2011.0
+ Revision: 609167
- rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.250.0-1mdv2010.0
+ Revision: 405599
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.25-6mdv2009.0
+ Revision: 241984
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.25-4mdv2008.0
+ Revision: 25461
- rebuild

* Mon May 07 2007 Olivier Thauvin <nanardon@mandriva.org> 0.25-3mdv2008.0
+ Revision: 23806
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.25-2mdk
- Fix SPEC according to Perl Policy
	- Source URL

* Sun Jan 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.25-1mdk
- 0.25

* Thu Dec 02 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.24-2mdk
- filter out perl(Error)

* Thu Dec 02 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.24-1mdk
- initial mandrake package

