Summary:	Glade to OCaml compiler
Summary(pl.UTF-8):   Kompilator Glade do OCamla
Name:		ocaml-mlglade
Version:	0.9
Release:	3
License:	LGPL but see LICENSE
Group:		Development/Building
Vendor:		Benjamin Monate <Benjamin.Monate@lri.fr>
URL:		http://www.lix.polytechnique.fr/Labo/Benjamin.Monate/mlglade/
Source0:	http://www.lix.polytechnique.fr/Labo/Benjamin.Monate/mlglade/mlglade-%{version}.tgz
# Source0-md5:	cec50caaf0a7fbcb332cdd2963816511
BuildRequires:	autoconf
BuildRequires:	hevea >= 1.06-3
BuildRequires:	ocaml >= 3.07
# note: it is not required to build, just to use
Requires:	ocaml-lablgtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mlglade is a tool to translate a Glade XML file into a set of modules
for OCaml.

%description -l pl.UTF-8
Mlglade jest narzędziem do tłumaczenia plików w formacie XML
stworzonych przez Glade w zbiór modułów dla OCamla.

%prep
%setup -q -n mlglade

%build
# this doesn't really matter (package makes little use of autoconf)
%{__autoconf}
%configure
sed -e 's/-g//' Makefile > Makefile.tmp
mv -f Makefile.tmp Makefile
%{__make}
%{__make} docs

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install mlglade.opt $RPM_BUILD_ROOT%{_bindir}/mlglade
install mlglade.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS README CHANGES LICENCE TODO tutorial/*.html tutorial/*.png
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
