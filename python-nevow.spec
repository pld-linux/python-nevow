%define		module	nevow
%define		version_in_filename	0.3
Summary:	Web application templating system
Summary(pl):	System szablonów do tworzenia stron WWW
Name:		python-%{module}
Version:	0.3.0
Release:	1
Epoch:		1
License:	LGPL
Group:		Libraries/Python
Source0:	http://nevow.com/releases/%{version}/%{module}-%{version_in_filename}.tar.gz
# Source0-md5:	c203da567b3c201dc1bc3ad14de1c2a6
URL:		http://nevow.com/
BuildRequires:	python-devel >= 2.3
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

%description -l pl
Nevow jest systemem szablonów wspomagaj±cym tworzenie aplikacji
webowych, bazuj±cym na pomys³ach zawartych w rozwijanym w ramach
projektu Twisted pakiecie Woven. G³ównym zadaniem Nevow jest
umo¿liwienie deweloperowi odseparowanie kodu szablonu HTML od logiki
biznesowej i logiki prezentacyjnej tworzonego systemu. Nevow rozdziela
kod na funkcje zarz±dzania danymi oraz ich wy¶wietlania, co jest
uproszczon± wersj± wzroca projektowego MVC. Na Nevow sk³ada siê zbiór
ró¿nych funkcjonalno¶ci, które mog± byæ u¿ywane osobno albo jako
ca³o¶ciwe rozwi±zanie wspomagaj±ce tworzenie aplikacji webowych:

- szablony XHTML: nie zawieraj± logiki programistycznej, jedynie
  wierzcho³ki tagowane atrybutami przestrzeni nazw nevow,
- funkcje zarz±dzania danymi i wy¶wietlaniem: uproszczenie wzorca
  projektowego Model-Widok-Kontroler (MVC),
- stan: sk³adnia wyra¿ania elementów jêzyka XML w czystym Pythonie w
  oparciu o s-wyra¿enia,
- formless: opisywanie typów obiektów mog±cych byæ argumentami
  tworzonych metod klas, weryfikacji i poprawiania znakowych danych
  wej¶ciowych od klientów WWW lub innych ¼róde³ oraz automatyczne
  wywo³ywanie w³asnych metod po poprawnej weryfikacji,
- freeform: renderowanie formularzy HTML oparte o opisy typów
  formless, akceptacja formularzy dostarczonych przez klienta, analiza
  ich zawarto¶ci w oparciu o mechanizm weryfikatorów formless oraz
  tworzenie komunikatów o b³êdach podczas nieudanej weryfikacji
  formularza,
- livepage: miêdzyplatformowy "klej" JavaScript umo¿liwiaj±cy
  przesy³anie efektów ubocznych pracy klienta do serwera i odwrotnie po
  za³adowaniu strony bez konieczno¶ci jej od¶wie¿ania.

%package doc
Summary:	Documentation files for Python nevow module
Summary(pl):	Dokumentacja do modu³u Pythona nevow
Group:		Libraries/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description doc
This package contains documentation files for nevow module.

%description doc -l pl
Pakiet zawieraj±cy dokumentacjê do modu³u Pythona nevow.

%package examples
Summary:	Example programs for Python nevow module
Summary(pl):	Programy przyk³adowe do modu³u Pythona nevow
Group:		Development/Languages/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description examples
This package contains example programs for Python nevow module.

%description examples -l pl
Pakiet zawieraj±cy programy przyk³adowe dla modu³u Pythona nevow.

%prep
%setup -q -n %{module}-%{version_in_filename}

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

mv $RPM_BUILD_ROOT%{py_sitescriptdir}/Nevow/* $RPM_BUILD_ROOT%{py_sitescriptdir}/
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/Nevow*

cp -ar examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/nevow
%{py_sitescriptdir}/formless

%files doc
%defattr(644,root,root,755)
%doc doc/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
