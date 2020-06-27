%define modname	Test-Unit
%define modver	0.25

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Error\\)'
%else
%define _requires_exceptions perl(Error)
%endif

Summary:	Test::Unit::TestCase - unit testing framework base class
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	18
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Test::Unit::TestCase is the 'workhorse' of the PerlUnit framework.
When writing tests, you generally subclass Test::Unit::TestCase,
write set_up and tear_down functions if you need them, a bunch of
test_* test methods, then do

%prep
%setup -qn %{modname}-%{modver}

# perl path hack
find . -type f | xargs perl -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build OPTIMIZE="%{optflags}"

%install
%make_install

%files
%doc AUTHORS ChangeLog Changes README doc examples
%{perl_vendorlib}/Test/*.p*
%{perl_vendorlib}/Test/Unit
%{_mandir}/man3/*

