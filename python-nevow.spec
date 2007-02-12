%define		module	nevow
Summary:	Web application templating system
Summary(pl.UTF-8):   System szablonów do tworzenia stron WWW
Name:		python-%{module}
Version:	0.4.1
Release:	1
Epoch:		1
License:	LGPL
Group:		Libraries/Python
Source0:	http://nevow.com/releases/%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	a7402e4571a23b99c59ce4e7d354f7ff
URL:		http://nevow.com/
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python-modules
Requires:	python >= 2.3
Requires:	python-Twisted >= 1.3.0
Obsoletes:	Quotient-nevow
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nevow is a next-generation web application templating system, based on
the ideas developed in the Twisted Woven package. Its main focus is on
separating the HTML template from both the business logic and the
display logic, while allowing the programmer to write pure Python code
as much as possible. It separates your code into 'data' and 'render'
functions, a simplified implementation of traditional MVC. It has
various parts which can be used individually or as a whole, integrated
web solution:
- XHTML templates: contain no programming logic, only nodes tagged
  with nevow attributes,
- data/render methods: simplified MVC,
- stan: An s-expression-like syntax for expressing xml in pure Python,
- formless: For describing the types of objects which may be passed to
  methods of your classes, validating and coercing string input from
  either web or command-line sources, and calling your methods
  automatically once validation passes,
- freeform: For rendering web forms based on formless type
  descriptions, accepting form posts and passing them to formless
  validators, and rendering error forms in the event validation fails,
- livepage: Cross-browser JavaScript glue for sending client side
  events to the server and server side events to the client after the
  page has loaded, without causing the entire page to refresh.

%description -l pl.UTF-8
Nevow jest systemem szablonów wspomagającym tworzenie aplikacji WWW,
bazującym na pomysłach zawartych w rozwijanym w ramach projektu
Twisted pakiecie Woven. Głównym zadaniem Nevow jest umożliwienie
deweloperowi odseparowanie kodu szablonu HTML od logiki biznesowej i
logiki prezentacyjnej tworzonego systemu. Nevow rozdziela kod na
funkcje zarządzania danymi oraz ich wyświetlania, co jest uproszczoną
wersją wzroca projektowego MVC. Na Nevow składa się zbiór różnych
funkcjonalności, które mogą być używane osobno albo jako całościwe
rozwiązanie wspomagające tworzenie aplikacji WWW:

- szablony XHTML: nie zawierają logiki programistycznej, jedynie
  wierzchołki tagowane atrybutami przestrzeni nazw nevow,
- funkcje zarządzania danymi i wyświetlaniem: uproszczenie wzorca
  projektowego Model-Widok-Kontroler (MVC),
- stan: składnia wyrażania elementów języka XML w czystym Pythonie w
  oparciu o s-wyrażenia,
- formless: opisywanie typów obiektów mogących być argumentami
  tworzonych metod klas, weryfikacji i poprawiania znakowych danych
  wejściowych od klientów WWW lub innych źródeł oraz automatyczne
  wywoływanie własnych metod po poprawnej weryfikacji,
- freeform: renderowanie formularzy HTML oparte o opisy typów
  formless, akceptacja formularzy dostarczonych przez klienta, analiza
  ich zawartości w oparciu o mechanizm weryfikatorów formless oraz
  tworzenie komunikatów o błędach podczas nieudanej weryfikacji
  formularza,
- livepage: międzyplatformowy "klej" JavaScript umożliwiający
  przesyłanie efektów ubocznych pracy klienta do serwera i odwrotnie po
  załadowaniu strony bez konieczności jej odświeżania.

%package doc
Summary:	Documentation files for Python nevow module
Summary(pl.UTF-8):   Dokumentacja do modułu Pythona nevow
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description doc
This package contains documentation files for nevow module.

%description doc -l pl.UTF-8
Pakiet zawierający dokumentację do modułu Pythona nevow.

%package examples
Summary:	Example programs for Python nevow module
Summary(pl.UTF-8):   Programy przykładowe do modułu Pythona nevow
Group:		Development/Languages/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description examples
This package contains example programs for Python nevow module.

%description examples -l pl.UTF-8
Pakiet zawierający programy przykładowe dla modułu Pythona nevow.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitescriptdir},%{_examplesdir}/%{name}-%{version},%{_datadir}/%{name}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/nevow
%{py_sitescriptdir}/formless

%files doc
%defattr(644,root,root,755)
%doc doc/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
