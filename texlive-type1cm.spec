# revision 21820
# category Package
# catalog-ctan /macros/latex/contrib/type1cm
# catalog-date 2011-03-24 10:40:42 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-type1cm
Version:	20110324
Release:	1
Summary:	Arbitrary size font selection in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/type1cm
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/type1cm.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/type1cm.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/type1cm.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
