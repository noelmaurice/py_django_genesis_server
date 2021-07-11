# genesis server

> Parse annotated VCF files and extract variant information.
>
> Manage variant with database and requests.
>
> Provide web services for doing request about variants (create variant, find variant samples, and so on)
>
> Provide API library for accessing to genesis server services
>

### Operating diagram for genesis server v0.3.0

![Operation diagram for genesis server v0.3.0](genesis/doc/img/operating_diagram_genesis_server_v0.3.0.png)

### Warning

There is two versions of the python library pysam : on a windows system install **pysam-win**, and install **pysam** for
other systems.

## Run the Django project server

> python manage.py runserver

## Launch the tests of the project

> python manage.py test

## Import API library and use it in a simple python script file

> See the project documentation
>
> [Import API library and use it in a simple python script file](genesis/doc/api_server.md)
