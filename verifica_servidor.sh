#!/bin/bash

codigo_http=$(curl --write-out %{http_code} --silent --output /dev/null www.google.com.br)

echo "O servidor web está $codigo_http"

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