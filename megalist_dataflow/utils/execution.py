# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from enum import Enum
from typing import List

OK_STATUS = 'OK'

class DestinationType(Enum):
  CM_OFFLINE_CONVERSION, \
  ADS_OFFLINE_CONVERSION, \
  ADS_SSD_UPLOAD, \
  ADS_CUSTOMER_MATCH_CONTACT_INFO_UPLOAD, \
  ADS_CUSTOMER_MATCH_MOBILE_DEVICE_ID_UPLOAD, \
  ADS_CUSTOMER_MATCH_USER_ID_UPLOAD, \
  GA_USER_LIST_UPLOAD = range(7)


class SourceType(Enum):
  BIG_QUERY, \
  CSV = range(2)
  # TODO: CSV not yet implemented

class AccountConfig:
  def __init__(
    self,
    google_ads_account_id:str,
    google_analytics_account_id:str,
    campaign_manager_account_id:str,
    app_id:str
  ):
    self._google_ads_account_id = google_ads_account_id
    self._google_analytics_account_id = google_analytics_account_id
    self._campaign_manager_account_id = campaign_manager_account_id
    self._app_id = app_id

  @property
  def google_ads_account_id(self) -> str:
    return self._google_ads_account_id

  @property
  def google_analytics_account_id(self) -> str:
    return self._google_analytics_account_id

  @property
  def campaign_manager_account_id(self) -> str:
    return self._campaign_manager_account_id

  @property
  def app_id(self) -> str:
    return self._app_id

  def __str__(self) -> str:
    return f"[Account Config] Google Ads Customer Id: {self.google_ads_account_id}, Google Analytics Account Id: {self.google_analytics_account_id}, Campaign Manager Account Id: {self.campaign_manager_account_id}, Play Store App Id: {self.app_id}"

  def __eq__(self, other):
    return self.google_ads_account_id == other.google_ads_account_id \
           and self.google_analytics_account_id == other.google_analytics_account_id \
           and self.campaign_manager_account_id == other.campaign_manager_account_id \
           and self.app_id == other.app_id

  def __hash__(self):
    return hash((self.google_ads_account_id, self.google_analytics_account_id, 
                 self.campaign_manager_account_id, self.app_id))

class Source:
  def __init__(
    self,
    source_name:str,
    source_type:SourceType,
    source_metadata:List[str]
  ):
    self._source_name = source_name
    self._source_type = source_type
    self._source_metadata = source_metadata

  @property
  def source_name(self) -> str:
    return self._source_name

  @property
  def source_type(self) -> SourceType:
    return self._source_type

  @property
  def source_metadata(self) -> List[str]:
    return self._source_metadata

  def __eq__(self, other):
    return self.source_name == other.source_name \
           and self.source_type == other.source_type \
           and self.source_metadata == other.source_metadata

  def __hash__(self):
    return hash((self.source_name, self.source_type, self.source_metadata))

class Destination:
  def __init__(
      self,
      destination_name:str,
      destination_type:DestinationType,
      destination_metadata:List[str]
    ):
    self._destination_name = destination_name
    self._destination_type = destination_type
    self._destination_metadata = destination_metadata

  @property
  def destination_name(self) -> str:
    return self._destination_name

  @property
  def destination_type(self) -> DestinationType:
    return self._destination_type

  @property
  def destination_metadata(self) -> List[str]:
    return self._destination_metadata

  def __eq__(self, other) -> bool:
    return  self.destination_name == other.destination_name \
          and self.destination_metadata == other.destination_metadata

  def __hash__(self):
    return hash((self.destination_name, self.destination_type, self.destination_metadata))


class Execution:
  def __init__(
      self,
      account_config:AccountConfig,
      source:Source,
      destination:Destination
  ):
    self._account_config = account_config
    self._source = source
    self._destination = destination

  @property
  def source(self) -> Source:
    return self._source

  @property
  def destination(self) -> Destination:
    return self._destination

  @property
  def account_config(self) -> AccountConfig:
    return self._account_config

  def __str__(self):
    return 'Origin name: {}. Action: {}. Destination name: {}'.format(self.source.source_name, self.destination.destination_type,
                                                                      self.destination.destination_name)

  def __eq__(self, other):
    return self.source == other.source \
           and self.destination == other.destination \
           and self.account_config == other.account_config

  def __hash__(self):
    return hash((self.source, self.destination, self.account_config))
