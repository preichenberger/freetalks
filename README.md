Freetalks
=========

Freetalks is a video catalog of talks and lectures.

### Development Data

Run tests:

    nosetests --with-gae --gae-lib-root=/PATH/TO/google_appengine

Go to [http://localhost:8080/_ah/admin/interactive Development Console] and run
the follow:

    from tests.fixtures import dataset
    dataset.setup()

### Licenses

This work is licensed under the MIT License (see the LICENSE file).
