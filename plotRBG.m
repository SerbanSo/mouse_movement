## Copyright (C) 2019 valky
## 
## This program is free software: you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see
## <https://www.gnu.org/licenses/>.

## -*- texinfo -*- 
## @deftypefn {} {@var{retval} =} plotRBG (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: valky <valky@DESKTOP-DIP0C0L>
## Created: 2019-09-05

function plotRBG()
  x = [0 : 0.01 : 2];
  R = max(0, x - 1);
  B = max(0, 1 - x);
  G = 1 - R - B;
  plot(x, R, "r", x, B, "b", x, G, "g")
  
  colors = zeros(201, 3);
  colors(:, 1) = R;
  colors(:, 2) = G;
  colors(:, 3) = B;
  figure(2);
  rgbplot(colors, "composite")
endfunction
