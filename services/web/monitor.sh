#!/bin/bash
UP=$(pgrep mysql | wc -l );
if [ $UP -ne 0 ];
then
        echo  " MySQL está fora do ar. " ;
        service sudo mysql start

else
        echo  "Está tudo bem.";
        echo $UP;
fi
exec "$@"