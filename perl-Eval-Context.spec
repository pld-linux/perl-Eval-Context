#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Eval
%define	pnam	Context
Summary:	Eval::Context - Evalute Perl code in context wraper
Summary(pl.UTF-8):	Eval::Context - wykonywanie kodu perlowego w kontekstowym obudowaniu
Name:		perl-Eval-Context
Version:	0.09.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/N/NK/NKH/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d13cabeb22d73d755634004b612f5cee
# https://rt.cpan.org/Public/Ticket/Attachment/1222240/645514/hash-randomization.patch
Patch0:		%{name}-hash-randomization.patch
URL:		http://search.cpan.org/dist/Eval-Context/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Data-Compare
BuildRequires:	perl-Data-TreeDumper
BuildRequires:	perl-Directory-Scratch-Structured
BuildRequires:	perl-File-Slurp
BuildRequires:	perl-Package-Generator
BuildRequires:	perl-Readonly
BuildRequires:	perl-Safe >= 2.16
BuildRequires:	perl-Sub-Exporter
BuildRequires:	perl-Sub-Install
BuildRequires:	perl-Test-Block
# disabled as of 0.09.x
#BuildRequires:	perl-Test-Dependencies
BuildRequires:	perl-Test-Distribution
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-NoWarnings
BuildRequires:	perl-Test-Output
BuildRequires:	perl-Test-Perl-Critic
BuildRequires:	perl-Test-Pod
BuildRequires:	perl-Test-Pod-Coverage
BuildRequires:	perl-Test-Strict
BuildRequires:	perl-Test-Warn
BuildRequires:	perl-Text-Diff
BuildRequires:	perl-version >= 0.5
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module define a subroutine that let you evaluate Perl code in a
specific context. The code can be passed directly as a string or as a
file name to read from. It also provides some subroutines to let you
define and optionally share variables and subroutines between your
code and the code you wish to evaluate. Finally there is some support
for running your code in a safe compartment.

%description -l pl.UTF-8
Ten moduł definiuje procedurę pozwalającą na wykonywanie kodu
perlowego w określonym kontekście. Kod może być przekazany
bezpośrednio jako łańcuch znaków lub jako nazwa pliku do odczytu.
Moduł udostępnia także funkcje pozwalające definiować i opcjonalnie
współdzielić zmienne i procedury między kodem własnym i tym, który ma
zostać wykonany. Daje także pewne możliwości wykonywania kodu w
bezpiecznym środowisku.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README Todo.txt
%{perl_vendorlib}/Eval/Context.pm
%{_mandir}/man3/Eval::Context.3pm*
