# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
import proto  # type: ignore

from google.protobuf import field_mask_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2beta1",
    manifest={
        "Agent",
        "GetAgentRequest",
        "SetAgentRequest",
        "DeleteAgentRequest",
        "SubAgent",
        "SearchAgentsRequest",
        "SearchAgentsResponse",
        "TrainAgentRequest",
        "ExportAgentRequest",
        "ExportAgentResponse",
        "ImportAgentRequest",
        "RestoreAgentRequest",
        "GetValidationResultRequest",
    },
)


class Agent(proto.Message):
    r"""A Dialogflow agent is a virtual agent that handles conversations
    with your end-users. It is a natural language understanding module
    that understands the nuances of human language. Dialogflow
    translates end-user text or audio during a conversation to
    structured data that your apps and services can understand. You
    design and build a Dialogflow agent to handle the types of
    conversations required for your system.

    For more information about agents, see the `Agent
    guide <https://cloud.google.com/dialogflow/docs/agents-overview>`__.

    Attributes:
        parent (str):
            Required. The project of this agent. Format:
            ``projects/<Project ID>`` or
            ``projects/<Project ID>/locations/<Location ID>``
        display_name (str):
            Required. The name of this agent.
        default_language_code (str):
            Required. The default language of the agent as a language
            tag. See `Language
            Support <https://cloud.google.com/dialogflow/docs/reference/language>`__
            for a list of the currently supported language codes. This
            field cannot be set by the ``Update`` method.
        supported_language_codes (Sequence[str]):
            Optional. The list of all languages supported by this agent
            (except for the ``default_language_code``).
        time_zone (str):
            Required. The time zone of this agent from the `time zone
            database <https://www.iana.org/time-zones>`__, e.g.,
            America/New_York, Europe/Paris.
        description (str):
            Optional. The description of this agent.
            The maximum length is 500 characters. If
            exceeded, the request is rejected.
        avatar_uri (str):
            Optional. The URI of the agent's avatar. Avatars are used
            throughout the Dialogflow console and in the self-hosted
            `Web
            Demo <https://cloud.google.com/dialogflow/docs/integrations/web-demo>`__
            integration.
        enable_logging (bool):
            Optional. Determines whether this agent
            should log conversation queries.
        match_mode (google.cloud.dialogflow_v2beta1.types.Agent.MatchMode):
            Optional. Determines how intents are detected
            from user queries.
        classification_threshold (float):
            Optional. To filter out false positive
            results and still get variety in matched natural
            language inputs for your agent, you can tune the
            machine learning classification threshold. If
            the returned score value is less than the
            threshold value, then a fallback intent will be
            triggered or, if there are no fallback intents
            defined, no intent will be triggered. The score
            values range from 0.0 (completely uncertain) to
            1.0 (completely certain). If set to 0.0, the
            default of 0.3 is used.
        api_version (google.cloud.dialogflow_v2beta1.types.Agent.ApiVersion):
            Optional. API version displayed in Dialogflow
            console. If not specified, V2 API is assumed.
            Clients are free to query different service
            endpoints for different API versions. However,
            bots connectors and webhook calls will follow
            the specified API version.
        tier (google.cloud.dialogflow_v2beta1.types.Agent.Tier):
            Optional. The agent tier. If not specified, TIER_STANDARD is
            assumed.
    """

    class MatchMode(proto.Enum):
        r"""Match mode determines how intents are detected from user
        queries.
        """
        MATCH_MODE_UNSPECIFIED = 0
        MATCH_MODE_HYBRID = 1
        MATCH_MODE_ML_ONLY = 2

    class ApiVersion(proto.Enum):
        r"""API version for the agent."""
        API_VERSION_UNSPECIFIED = 0
        API_VERSION_V1 = 1
        API_VERSION_V2 = 2
        API_VERSION_V2_BETA_1 = 3

    class Tier(proto.Enum):
        r"""Represents the agent tier."""
        TIER_UNSPECIFIED = 0
        TIER_STANDARD = 1
        TIER_ENTERPRISE = 2
        TIER_ENTERPRISE_PLUS = 3

    parent = proto.Field(proto.STRING, number=1,)
    display_name = proto.Field(proto.STRING, number=2,)
    default_language_code = proto.Field(proto.STRING, number=3,)
    supported_language_codes = proto.RepeatedField(proto.STRING, number=4,)
    time_zone = proto.Field(proto.STRING, number=5,)
    description = proto.Field(proto.STRING, number=6,)
    avatar_uri = proto.Field(proto.STRING, number=7,)
    enable_logging = proto.Field(proto.BOOL, number=8,)
    match_mode = proto.Field(proto.ENUM, number=9, enum=MatchMode,)
    classification_threshold = proto.Field(proto.FLOAT, number=10,)
    api_version = proto.Field(proto.ENUM, number=14, enum=ApiVersion,)
    tier = proto.Field(proto.ENUM, number=15, enum=Tier,)


class GetAgentRequest(proto.Message):
    r"""The request message for
    [Agents.GetAgent][google.cloud.dialogflow.v2beta1.Agents.GetAgent].

    Attributes:
        parent (str):
            Required. The project that the agent to fetch is associated
            with. Format: ``projects/<Project ID>`` or
            ``projects/<Project ID>/locations/<Location ID>``.
    """

    parent = proto.Field(proto.STRING, number=1,)


class SetAgentRequest(proto.Message):
    r"""The request message for
    [Agents.SetAgent][google.cloud.dialogflow.v2beta1.Agents.SetAgent].

    Attributes:
        agent (google.cloud.dialogflow_v2beta1.types.Agent):
            Required. The agent to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The mask to control which fields
            get updated.
    """

    agent = proto.Field(proto.MESSAGE, number=1, message="Agent",)
    update_mask = proto.Field(
        proto.MESSAGE, number=2, message=field_mask_pb2.FieldMask,
    )


class DeleteAgentRequest(proto.Message):
    r"""The request message for
    [Agents.DeleteAgent][google.cloud.dialogflow.v2beta1.Agents.DeleteAgent].

    Attributes:
        parent (str):
            Required. The project that the agent to delete is associated
            with. Format: ``projects/<Project ID>`` or
            ``projects/<Project ID>/locations/<Location ID>``.
    """

    parent = proto.Field(proto.STRING, number=1,)


class SubAgent(proto.Message):
    r"""Contains basic configuration for a sub-agent.

    Attributes:
        project (str):
            Required. The project of this agent. Format:
            ``projects/<Project ID>`` or
            ``projects/<Project ID>/locations/<Location ID>``.
        environment (str):
            Optional. The unique identifier (``environment name`` in
            dialogflow console) of this sub-agent environment. Assumes
            draft environment if ``environment`` is not set.
    """

    project = proto.Field(proto.STRING, number=1,)
    environment = proto.Field(proto.STRING, number=2,)


class SearchAgentsRequest(proto.Message):
    r"""The request message for
    [Agents.SearchAgents][google.cloud.dialogflow.v2beta1.Agents.SearchAgents].

    Attributes:
        parent (str):
            Required. The project to list agents from. Format:
            ``projects/<Project ID or '-'>`` or
            ``projects/<Project ID or '-'>/locations/<Location ID>``.
        page_size (int):
            Optional. The maximum number of items to
            return in a single page. By default 100 and at
            most 1000.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            list request.
    """

    parent = proto.Field(proto.STRING, number=1,)
    page_size = proto.Field(proto.INT32, number=2,)
    page_token = proto.Field(proto.STRING, number=3,)


class SearchAgentsResponse(proto.Message):
    r"""The response message for
    [Agents.SearchAgents][google.cloud.dialogflow.v2beta1.Agents.SearchAgents].

    Attributes:
        agents (Sequence[google.cloud.dialogflow_v2beta1.types.Agent]):
            The list of agents. There will be a maximum number of items
            returned based on the page_size field in the request.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    agents = proto.RepeatedField(proto.MESSAGE, number=1, message="Agent",)
    next_page_token = proto.Field(proto.STRING, number=2,)


class TrainAgentRequest(proto.Message):
    r"""The request message for
    [Agents.TrainAgent][google.cloud.dialogflow.v2beta1.Agents.TrainAgent].

    Attributes:
        parent (str):
            Required. The project that the agent to train is associated
            with. Format: ``projects/<Project ID>`` or
            ``projects/<Project ID>/locations/<Location ID>``.
    """

    parent = proto.Field(proto.STRING, number=1,)


class ExportAgentRequest(proto.Message):
    r"""The request message for
    [Agents.ExportAgent][google.cloud.dialogflow.v2beta1.Agents.ExportAgent].

    Attributes:
        parent (str):
            Required. The project that the agent to export is associated
            with. Format: ``projects/<Project ID>`` or
            ``projects/<Project ID>/locations/<Location ID>``.
        agent_uri (str):
            Optional. The `Google Cloud
            Storage <https://cloud.google.com/storage/docs/>`__ URI to
            export the agent to. The format of this URI must be
            ``gs://<bucket-name>/<object-name>``. If left unspecified,
            the serialized agent is returned inline.
    """

    parent = proto.Field(proto.STRING, number=1,)
    agent_uri = proto.Field(proto.STRING, number=2,)


class ExportAgentResponse(proto.Message):
    r"""The response message for
    [Agents.ExportAgent][google.cloud.dialogflow.v2beta1.Agents.ExportAgent].

    Attributes:
        agent_uri (str):
            The URI to a file containing the exported agent. This field
            is populated only if ``agent_uri`` is specified in
            ``ExportAgentRequest``.
        agent_content (bytes):
            Zip compressed raw byte content for agent.
    """

    agent_uri = proto.Field(proto.STRING, number=1, oneof="agent",)
    agent_content = proto.Field(proto.BYTES, number=2, oneof="agent",)


class ImportAgentRequest(proto.Message):
    r"""The request message for
    [Agents.ImportAgent][google.cloud.dialogflow.v2beta1.Agents.ImportAgent].

    Attributes:
        parent (str):
            Required. The project that the agent to import is associated
            with. Format: ``projects/<Project ID>`` or
            ``projects/<Project ID>/locations/<Location ID>``.
        agent_uri (str):
            The URI to a Google Cloud Storage file
            containing the agent to import. Note: The URI
            must start with "gs://".
        agent_content (bytes):
            Zip compressed raw byte content for agent.
    """

    parent = proto.Field(proto.STRING, number=1,)
    agent_uri = proto.Field(proto.STRING, number=2, oneof="agent",)
    agent_content = proto.Field(proto.BYTES, number=3, oneof="agent",)


class RestoreAgentRequest(proto.Message):
    r"""The request message for
    [Agents.RestoreAgent][google.cloud.dialogflow.v2beta1.Agents.RestoreAgent].

    Attributes:
        parent (str):
            Required. The project that the agent to restore is
            associated with. Format: ``projects/<Project ID>`` or
            ``projects/<Project ID>/locations/<Location ID>``.
        agent_uri (str):
            The URI to a Google Cloud Storage file
            containing the agent to restore. Note: The URI
            must start with "gs://".
        agent_content (bytes):
            Zip compressed raw byte content for agent.
    """

    parent = proto.Field(proto.STRING, number=1,)
    agent_uri = proto.Field(proto.STRING, number=2, oneof="agent",)
    agent_content = proto.Field(proto.BYTES, number=3, oneof="agent",)


class GetValidationResultRequest(proto.Message):
    r"""The request message for
    [Agents.GetValidationResult][google.cloud.dialogflow.v2beta1.Agents.GetValidationResult].

    Attributes:
        parent (str):
            Required. The project that the agent is associated with.
            Format: ``projects/<Project ID>`` or
            ``projects/<Project ID>/locations/<Location ID>``.
        language_code (str):
            Optional. The language for which you want a validation
            result. If not specified, the agent's default language is
            used. `Many
            languages <https://cloud.google.com/dialogflow/docs/reference/language>`__
            are supported. Note: languages must be enabled in the agent
            before they can be used.
    """

    parent = proto.Field(proto.STRING, number=1,)
    language_code = proto.Field(proto.STRING, number=3,)


__all__ = tuple(sorted(__protobuf__.manifest))
