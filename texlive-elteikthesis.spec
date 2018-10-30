# revision 22513
# category Package
# catalog-ctan /macros/latex/contrib/elteikthesis
# catalog-date 2011-05-17 17:52:56 +0200
# catalog-license lppl1.2
# catalog-version 1.2
Name:		texlive-elteikthesis
Version:	1.2
Release:	12
Summary:	Thesis class for ELTE University Informatics wing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/elteikthesis
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elteikthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elteikthesis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elteikthesis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is not an official University class, and has not been
approved by the University.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/elteikthesis/elteikthesis.cls
%doc %{_texmfdistdir}/doc/latex/elteikthesis/README
%doc %{_texmfdistdir}/doc/latex/elteikthesis/elteikthesis.pdf
%doc %{_texmfdistdir}/doc/latex/elteikthesis/example.pdf
%doc %{_texmfdistdir}/doc/latex/elteikthesis/example.tex
%doc %{_texmfdistdir}/doc/latex/elteikthesis/pics/eltecimerszines.eps
%doc %{_texmfdistdir}/doc/latex/elteikthesis/pics/eltecimerszines.jpg
#- source
%doc %{_texmfdistdir}/source/latex/elteikthesis/elteikthesis.dtx
%doc %{_texmfdistdir}/source/latex/elteikthesis/elteikthesis.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 751408
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 718323
- texlive-elteikthesis
- texlive-elteikthesis
- texlive-elteikthesis
- texlive-elteikthesis

