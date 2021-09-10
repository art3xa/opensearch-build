# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.

import unittest
from unittest.mock import MagicMock

from ci_workflow.check_gradle_publish_to_maven_local import \
    CheckGradlePublishToMavenLocal


class TestCheckGradlePublishToMavenLocal(unittest.TestCase):
    def test_executes_gradle_command(self):
        check = CheckGradlePublishToMavenLocal(
            component=MagicMock(),
            git_repo=MagicMock(),
            version="1.1.0",
            arch="x86",
            snapshot=False,
        )
        check.check()
        check.git_repo.execute.assert_called_once_with(
            "./gradlew publishToMavenLocal -Dopensearch.version=1.1.0 -Dbuild.snapshot=false"
        )

    def test_executes_gradle_command_snapshot(self):
        check = CheckGradlePublishToMavenLocal(
            component=MagicMock(),
            git_repo=MagicMock(),
            version="1.1.0",
            arch="x86",
            snapshot=True,
        )
        check.check()
        check.git_repo.execute.assert_called_once_with(
            "./gradlew publishToMavenLocal -Dopensearch.version=1.1.0-SNAPSHOT -Dbuild.snapshot=true"
        )
