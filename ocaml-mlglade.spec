Summary:	Glade to OCaml compiler
Summary(pl):	Kompilator Glade do OCamla
Name:		ocaml-mlglade
Version:	0.5
Release:	1
License:	LGPL
Group:		Development/Building
Vendor:		Benjamin Monate <Benjamin.Monate@lri.fr>
URL:		http://www.lri.fr/~monate/mlglade/
Source0:	http://www.lri.fr/~monate/mlglade/mlglade-%{version}.tgz
BuildRequires:	autoconf
BuildRequires:	hevea
BuildRequires:	ocaml >= 3.04
# note: it is not required to build, just to use
Requires:	ocaml-lablgtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mlglade is a tool to translate a Glade XML file into a set of modules
for OCaml.

%description -l pl
Mlglade jest narzêdziem do t³umaczenia plików w formacie XML
stworzonych przez Glade w zbiór modu³ów dla OCamla.

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

gzip -9nf BUGS README CHANGES LICENCE TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz tutorial/*.html tutorial/*.png
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
