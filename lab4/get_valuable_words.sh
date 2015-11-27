echo '#!/usr/bin/python'
echo '# -*- coding: utf-8 -*-'
echo ''

echo 'data = {'
grep $2 $1 | sed "s/^.*,\(.*\),\(.*\)$/'\1':\2,/g"
echo '}'

echo ''

