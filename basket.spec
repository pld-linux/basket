%define		_alpha	Alpha1
%define		_alpha_m	C
%define		_alpha_f	%{_alpha}%{_alpha_m}
Summary:	A container for various types of data
Summary(pl):	Pojemnik na ró¿ne rodzaje danych
Name:		basket
Version:	0.6.0
Release:	0.%{_alpha_f}.1
License:	GPL
Group:		Applications
# from	http://basket.kde.org/downloads/?file=%{name}-%{version}.tar.gz
Source0:	http://team.pld-linux.org/~djurban/kde/%{name}-%{version}%{_alpha_f}.tar.gz
# Source0-md5:	6cda67414de6bc3757a591225ee80c2a
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
Ta aplikacja udostêpnia dowoln± liczbê koszyków (szuflad) i pozwala
przeci±gaæ i upuszczaæ na nie ró¿ne obiekty (tekst, URL-e, obrazki,
d¼wiêki...). Obiekty mog± byæ modyfikowane, kopiowane, przeci±gane...
Mo¿na je uk³adaæ jak tylko chcemy. Ta aplikacja mo¿e byæ u¿ywana do
szybkiego upuszczania obiektów WWW (odno¶ników, tekstu, obrazków...)
lub notatek (tekstów albo obrazków, pó¼niej d¼wiêków), a tak¿e
uwalniania pulpitu ze ¶mieci.

%prep
%setup -q -n %{name}-%{version}%{_alpha}
%{__sed} -i -e 's,\$(TOPSUBDIRS),doc po src,'  Makefile.am

%build
cp -f /usr/share/automake/config.sub admin
#export UNSERMAKE=/usr/share/unsermake/unsermake
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
