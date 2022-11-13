Name:		texlive-type1cm
Version:	21820
Release:	1
Summary:	Arbitrary size font selection in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/type1cm
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/type1cm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/type1cm.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/type1cm.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
LaTeX, by default, restricts the sizes at which you can use its
default computer modern fonts, to a fixed set of discrete sizes
(effectively, a set specified by Knuth). The type1cm package
removes this restriction; this is particularly useful when
using scalable versions of the cm fonts (Bakoma, or the
versions from BSR/Y&Y, or True Type versions from Kinch, PCTeX,
etc.). In fact, since modern distributions will automatically
generate any bitmap font you might need, type1cm has wider
application than just those using scaleable versions of the
fonts. Note that the LaTeX distribution now contains a package
fix-cm, which performs the task of type1cm, as well as doing
the same job for T1- and TS1-encoded ec fonts.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/type1cm/type1cm.sty
%doc %{_texmfdistdir}/doc/latex/type1cm/type1cm-doc.pdf
%doc %{_texmfdistdir}/doc/latex/type1cm/type1cm-doc.tex
%doc %{_texmfdistdir}/doc/latex/type1cm/type1cm.txt
#- source
%doc %{_texmfdistdir}/source/latex/type1cm/type1cm.fdd
%doc %{_texmfdistdir}/source/latex/type1cm/type1cm.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
