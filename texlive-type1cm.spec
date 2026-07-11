%global tl_name type1cm
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Arbitrary size font selection in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/type1cm
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/type1cm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/type1cm.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/type1cm.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LaTeX, by default, restricts the sizes at which you can use its default
computer modern fonts, to a fixed set of discrete sizes (effectively, a
set specified by Knuth). The type1cm package removes this restriction;
this is particularly useful when using scalable versions of the cm fonts
(Bakoma, or the versions from BSR/Y&Y, or True Type versions from Kinch,
PCTeX, etc.). In fact, since modern distributions will automatically
generate any bitmap font you might need, type1cm has wider application
than just those using scaleable versions of the fonts. Note that the
LaTeX distribution now contains a package fix-cm, which performs the
task of type1cm, as well as doing the same job for T1- and TS1-encoded
ec fonts.

