pipeline
========

handy data handling script
------------------------


`filter`

usage:

1. vim filter.log

        > 12345
        > 2345
        > 345

2. cat filter.log | filter like ".3.5"

        > 23456

3. cat filter.log | filter in filter.log

        > 12345
        > 2345
        > 345
