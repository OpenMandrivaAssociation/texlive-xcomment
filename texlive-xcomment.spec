# revision 20031
# category Package
# catalog-ctan /macros/generic/xcomment
# catalog-date 2010-09-08 12:33:34 +0200
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-xcomment
Version:	1.3
Release:	9
Summary:	Allows selected environments to be included/excluded
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/xcomment
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcomment.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcomment.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines an environment that only typesets specified
environments within its scope. So, for example, if you want
nothing but the figure and table environments in your document,
you can enclose the whole document with an xcomment environment
that excludes everything but. This is a lot easier than
excluding the chunks of text between the environments you want,
or creating an entire document containing only those
environments. The package was previously part of the seminar
bundle for typesetting presentations.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/xcomment/xcomment.sty
%{_texmfdistdir}/tex/generic/xcomment/xcomment.tex
%doc %{_texmfdistdir}/doc/generic/xcomment/Changes
%doc %{_texmfdistdir}/doc/generic/xcomment/Makefile
%doc %{_texmfdistdir}/doc/generic/xcomment/README
%doc %{_texmfdistdir}/doc/generic/xcomment/xcomment-doc.pdf
%doc %{_texmfdistdir}/doc/generic/xcomment/xcomment-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 757584
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 719919
- texlive-xcomment
- texlive-xcomment
- texlive-xcomment

