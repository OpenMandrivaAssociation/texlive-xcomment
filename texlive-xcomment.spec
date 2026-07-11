%global tl_name xcomment
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.40
Release:	%{tl_revision}.1
Summary:	Allows selected environments to be included/excluded
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xcomment
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xcomment.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xcomment.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines an environment that only typesets specified
environments within its scope. So, for example, if you want nothing but
the figure and table environments in your document, you can enclose the
whole document with an xcomment environment that excludes everything
but. This is a lot easier than excluding the chunks of text between the
environments you want, or creating an entire document containing only
those environments. The package was previously part of the seminar
bundle for typesetting presentations.

