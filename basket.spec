%define		_beta	beta2
Summary:	A container for various types of data
Summary(pl):	Pojemnik na r�ne rodzaje danych
Name:		basket
Version:	0.5.0
Release:	0.%{_beta}.1
License:	GPL
Group:		Applications
Source0:	http://slaout.linux62.org/basket/downloads/%{name}-%{version}-%{_beta}.tar.gz
# Source0-md5:	b5d4a91948b08090b0c9691973cd0204
URL:		http://basket.kde.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRequires:	unsermake >= 040805
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This application provide as many baskets (drawers) as you wish, and
you can drag and drop various objects (text, URLs, images, sounds...)
into its. Objects can be edited, copied, dragged... So, you can
arrange them as you want! This application can be used to quickly
drop web objects (link, text, images...) or notes (texts or images
and, later, sound), as well as free your clutered desktop (if any).

%description -l pl
Ta aplikacja udost�pnia dowoln� liczb� koszyk�w (szuflad) i pozwala
przeci�ga� i upuszcza� na nie r�ne obiekty (tekst, URL-e, obrazki,
d�wi�ki...). Obiekty mog� by� modyfikowane, kopiowane, przeci�gane...
Mo�na je uk�ada� jak tylko chcemy. Ta aplikacja mo�e by� u�ywana do
szybkiego upuszczania obiekt�w WWW (odno�nik�w, tekstu, obrazk�w...)
lub notatek (tekst�w albo obrazk�w, p�niej d�wi�k�w), a tak�e
uwalniania pulpitu ze �mieci.

%prep
%setup -q -n %{name}-%{version}-%{_beta}
%{__sed} -i -e 's,\$(TOPSUBDIRS),doc po src,'  Makefile.am

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}
mv $RPM_BUILD_ROOT{%{_datadir}/applnk/Utilities/basket.desktop,%{_desktopdir}}
echo "Categories=Qt;KDE;Utility;" >> $RPM_BUILD_ROOT%{_desktopdir}/basket.desktop

%find_lang basket --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f basket.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_datadir}/apps/basket
%{_iconsdir}/crystalsvg/*x*/*/*.png
%{_iconsdir}/crystalsvg/scalable/apps/*.svg
