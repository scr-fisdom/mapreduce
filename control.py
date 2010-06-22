#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""API for controlling MapReduce execution outside of MapReduce framework."""


__all__ = ["start_map"]

import google

from mapreduce import model
from mapreduce import handlers


def start_map(name,
              handler_spec,
              reader_spec,
              reader_parameters,
              shard_count,
              base_path="/mapreduce",
              queue_name="default"):
  """Start a new, mapper-only mapreduce.

  Args:
    name: mapreduce name. Used only for display purposes.
    handler_spec: fully qualified name of mapper handler function/class to call.
    reader_spec: fully qualified name of mapper reader to use
    reader_parameters: dictionary of parameters to pass to reader. These are
      reader-specific.
    shard_count: number of shards to create.
    base_path: base path of mapreduce library handler specified in app.yaml.
      "/mapreduce" by default.
    queue_name: executor queue name to be used for mapreduce tasks.

  Returns:
    mapreduce id as string.
  """
  mapper_spec = model.MapperSpec(handler_spec, reader_spec, reader_parameters,
                                 shard_count)

  return handlers.StartJobHandler._start_map(name, mapper_spec,
                                             base_path=base_path,
                                             queue_name=queue_name)

