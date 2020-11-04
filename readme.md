Decoder vnt file format (Mobile Phone VNote Sony Ericsson Format)
=============================

Быстрый старт
-----------

Запускать командой:

        python vnt_decoder.py test.vnt

Выходные файлы будут появлятся в текущей директории
В данном случае выходной файл будет test.vnt.txt

Пример, на входе test.vnt:

        BEGIN:VNOTE
        VERSION:1.1
        BODY;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:=D0=9F=D1=80=D0=B8=D0=B2=D0=B5=D1=82=20=D0=BC=D0=B8=D1=80=0A
        DCREATED:20201104T004634
        LAST-MODIFIED:20201104T004634
        END:VNOTE

На выходе test.vnt.txt:

        Привет мир
