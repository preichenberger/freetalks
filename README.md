Freetalks
=========

Freetalks is a catalog of free talks and lectures.

### Development

Run tests:

    nosetests --with-gae --gae-lib-root=/PATH/TO/google_appengine

To setup development data go to the [Development Console][console] and run the following:

    from tests.fixtures import dataset
    dataset.clear()
    dataset.setup()

### Licenses

This work is licensed under the MIT License (see the LICENSE file).

[console]: http://localhost:8080/_ah/admin/interactive
