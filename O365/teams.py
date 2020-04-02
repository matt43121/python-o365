import logging

from dateutil.parser import parse
from .utils import ApiComponent, TeamAsyncOperation

log = logging.getLogger(__name__)


class Team(ApiComponent):
    """ A Microsoft Teams team """

    _endpoints = {}

    def __init__(self, *, parent=None, con=None, **kwargs):
        """ A Microsoft Teams team

        :param parent: parent object
        :type parent: Teams
        :param Connection con: connection to use if no parent specified
        :param Protocol protocol: protocol to use if no parent specified
         (kwargs)
        :param str main_resource: use this resource instead of parent resource
         (kwargs)
        """
        if parent and con:
            raise ValueError('Need a parent or a connection but not both')
        self.con = parent.con if parent else con

        cloud_data = kwargs.get(self._cloud_data_key, {})

        self.object_id = cloud_data.get('id')

        # Choose the main_resource passed in kwargs over parent main_resource
        main_resource = kwargs.pop('main_resource', None) or (
            getattr(parent, 'main_resource', None) if parent else None)

        main_resource = '{}{}'.format(main_resource, '')

        super().__init__(
            protocol=parent.protocol if parent else kwargs.get('protocol'),
            main_resource=main_resource)

        self.display_name = cloud_data.get(self._cc('displayName'), '')
        self.description = cloud_data.get(self._cc('description'), '')
        self.is_archived = cloud_data.get(self._cc('isArchived'), '')
        self.web_url = cloud_data.get(self._cc('webUrl'), '')

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return 'Team: {}'.format(self.display_name)

    def __eq__(self, other):
        return self.object_id == other.object_id

class TeamAsync(ApiComponent):
    """ A Microsoft Teams Async Operation """

    _endpoints = {}

    def __init__(self, *, parent=None, con=None, **kwargs):
        """ A Microsoft Teams Async Operation

        :param parent: parent object
        :type parent: Teams
        :param Connection con: connection to use if no parent specified
        :param Protocol protocol: protocol to use if no parent specified
         (kwargs)
        :param str main_resource: use this resource instead of parent resource
         (kwargs)
        """
        if parent and con:
            raise ValueError('Need a parent or a connection but not both')
        self.con = parent.con if parent else con

        cloud_data = kwargs.get(self._cloud_data_key, {})

        self.object_id = cloud_data.get('id')

        # Choose the main_resource passed in kwargs over parent main_resource
        main_resource = kwargs.pop('main_resource', None) or (
            getattr(parent, 'main_resource', None) if parent else None)

        main_resource = '{}{}'.format(main_resource, '')

        super().__init__(
            protocol=parent.protocol if parent else kwargs.get('protocol'),
            main_resource=main_resource)

        self.operation_type = cloud_data.get(self._cc('operationType'), '')
        self.created_date_time = cloud_data.get(self._cc('createdDateTime'), '')
        self.status = cloud_data.get(self._cc('status'), '')
        self.last_action_date_time = cloud_data.get(self._cc('lastActionDateTime'), '')
        self.attempts_count = cloud_data.get(self._cc('attemptsCount'), '')
        self.target_resource_id = cloud_data.get(self._cc('targetResourceId'), '')
        self.target_resource_location = cloud_data.get(self._cc('targetResourceLocation'), '')
        self.error = cloud_data.get(self._cc('error'), '')

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return 'Team Async: {}'.format(self.operation_type)

    def __eq__(self, other):
        return self.object_id == other.object_id


class Channel(ApiComponent):
    """ A Microsoft Teams channel """

    _endpoints = {}

    def __init__(self, *, parent=None, con=None, **kwargs):
        """ A Microsoft Teams channel

        :param parent: parent object
        :type parent: Teams
        :param Connection con: connection to use if no parent specified
        :param Protocol protocol: protocol to use if no parent specified
         (kwargs)
        :param str main_resource: use this resource instead of parent resource
         (kwargs)
        """
        if parent and con:
            raise ValueError('Need a parent or a connection but not both')
        self.con = parent.con if parent else con

        cloud_data = kwargs.get(self._cloud_data_key, {})

        self.object_id = cloud_data.get('id')

        # Choose the main_resource passed in kwargs over parent main_resource
        main_resource = kwargs.pop('main_resource', None) or (
            getattr(parent, 'main_resource', None) if parent else None)

        main_resource = '{}{}'.format(main_resource, '')

        super().__init__(
            protocol=parent.protocol if parent else kwargs.get('protocol'),
            main_resource=main_resource)

        self.display_name = cloud_data.get(self._cc('displayName'), '')
        self.description = cloud_data.get('description')
        self.email = cloud_data.get('email')

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return 'Channel: {}'.format(self.display_name)

    def __eq__(self, other):
        return self.object_id == other.object_id


class App(ApiComponent):
    """ A Microsoft Teams app """

    _endpoints = {}

    def __init__(self, *, parent=None, con=None, **kwargs):
        """ A Microsoft Teams app

        :param parent: parent object
        :type parent: Teams
        :param Connection con: connection to use if no parent specified
        :param Protocol protocol: protocol to use if no parent specified
         (kwargs)
        :param str main_resource: use this resource instead of parent resource
         (kwargs)
        """
        if parent and con:
            raise ValueError('Need a parent or a connection but not both')
        self.con = parent.con if parent else con

        cloud_data = kwargs.get(self._cloud_data_key, {})

        self.object_id = cloud_data.get('id')

        # Choose the main_resource passed in kwargs over parent main_resource
        main_resource = kwargs.pop('main_resource', None) or (
            getattr(parent, 'main_resource', None) if parent else None)

        main_resource = '{}{}'.format(main_resource, '')

        super().__init__(
            protocol=parent.protocol if parent else kwargs.get('protocol'),
            main_resource=main_resource)

        self.app_definition = cloud_data.get(self._cc('teamsAppDefinition'), '')

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return 'App: {}'.format(self.app_definition['displayName'])

    def __eq__(self, other):
        return self.object_id == other.object_id


class Teams(ApiComponent):
    """ A microsoft teams class
        In order to use the API following permissions are required.
        Delegated (work or school account) - Group.Read.All, Group.ReadWrite.All
    """

    _endpoints = {
        'get_teams': '/teams/{team_id}',
        'get_my_teams': '/me/joinedTeams',
        'get_channels': '/teams/{team_id}/channels',
        'create_channel': '/teams/{team_id}/channels',
        'get_channel_info': '/teams/{team_id}/channels/{channel_id}',
        'get_apps_in_team': '/teams/{team_id}/installedApps?$expand=teamsAppDefinition',
        'create_team': '/groups/{group_id}/team',
        'clone_team': '/teams/{team_id}/clone',
        'archive_team': '/teams/{team_id}/archive',
        'unarchive_team': '/teams/{team_id}/unarchive',
        'installed_apps': '/teams/{team_id}/installedApps',
    }

    team_constructor = Team
    team_async_constructor = TeamAsync
    channel_constructor = Channel
    app_constructor = App

    def __init__(self, *, parent=None, con=None, **kwargs):
        """ A Teams object

        :param parent: parent object
        :type parent: Account
        :param Connection con: connection to use if no parent specified
        :param Protocol protocol: protocol to use if no parent specified
         (kwargs)
        :param str main_resource: use this resource instead of parent resource
         (kwargs)
        """
        if parent and con:
            raise ValueError('Need a parent or a connection but not both')
        self.con = parent.con if parent else con

        # Choose the main_resource passed in kwargs over the host_name
        main_resource = kwargs.pop('main_resource',
                                   '')  # defaults to blank resource
        super().__init__(
            protocol=parent.protocol if parent else kwargs.get('protocol'),
            main_resource=main_resource)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return 'Microsoft Teams'

    def get_my_teams(self, *args):
        """ Returns a list of teams that I am in

        :rtype: teams
        """

        url = self.build_url(self._endpoints.get('get_my_teams'))

        response = self.con.get(url)

        if not response:
            return None

        data = response.json()

        return [
            self.team_constructor(parent=self, **{self._cloud_data_key: site})
            for site in data.get('value', [])]

    def get_channels(self, team_id=None):
        """ Returns a list of channels of a specified team

        :param team_id: the team_id of the channel to be retrieved.

        :rtype: channels
        """

        if not team_id:
            raise RuntimeError('Provide the team_id')

        if team_id:
            # get channels by the team id
            url = self.build_url(
                self._endpoints.get('get_channels').format(team_id=team_id))

        response = self.con.get(url)

        if not response:
            return None

        data = response.json()

        return [
            self.channel_constructor(parent=self, **{self._cloud_data_key: site})
            for site in data.get('value', [])]

    def create_channel(self, team_id=None, display_name=None, description=None):
        """ Creates a channel within a specified team

        :param team_id: the team_id where the channel is created.

        :rtype: channel
        """

        if not team_id and display_name:
            raise RuntimeError('Provide the team_id and the display_name')

        if team_id:
            # get channels by the team id
            url = self.build_url(
                self._endpoints.get('get_channels').format(team_id=team_id))

        if display_name and description:
            data = {
                'displayName': display_name,
                'description': description,
            }
        else:
            data = {
                'displayName': display_name,
            }

        response = self.con.post(url, data=data)

        if not response:
            return None

        data = response.json()

        return self.channel_constructor(parent=self, **{self._cloud_data_key: data})

    def get_channel_info(self, team_id=None, channel_id=None):
        """ Returns the channel info for a given channel

        :param team_id: the team_id of the channel to get the info of.
        :param channel_id: the channel_id of the channel to get the info of.

        :rtype: channel
        """

        if not team_id and channel_id:
            raise RuntimeError('Provide the team_id and channel_id')

        if team_id:
            # get channels by the team id
            url = self.build_url(
                self._endpoints.get('get_channel_info').format(team_id=team_id, channel_id=channel_id))

        response = self.con.get(url)

        if not response:
            return None

        data = response.json()

        return self.channel_constructor(parent=self, **{self._cloud_data_key: data})

    def get_apps_in_team(self, team_id=None):
        """ Returns a list of apps of a specified team

        :param team_id: the team_id of the team to get the apps of.

        :rtype: apps
        """

        if team_id:
            # get channels by the team id
            url = self.build_url(
                self._endpoints.get('get_apps_in_team').format(team_id=team_id))
        else:
            raise RuntimeError('Provide the team_id')

        response = self.con.get(url)

        if not response:
            return None

        data = response.json()

        return [
            self.app_constructor(
                parent=self, **{self._cloud_data_key: site})
            for site in data.get('value', [])]

    def create_team(self, group_id=None):
        """ Creates a team under a group

        :param group_id: the group_id of the group that you want to create a team under.

        :rtype: team
        """

        if not group_id:
            raise RuntimeError('Provide the group_id')

        if group_id:
            url = self.build_url(
                self._endpoints.get('create_team').format(group_id=group_id))


        response = self.con.put(url)

        if not response:
            return None

        data = response.json()

        return self.team_constructor(parent=self, **{self._cloud_data_key: data})

    def get_team(self, team_id=None):
        """ Retrieve the properties and relationships of the specified team.

        :param team_id: the group_id of the group that you want to create a team under.

        :rtype: team
        """
        pass

    def update_team(self, team_id=None):
        """ Update the properties of the specified team.

        :param team_id: the group_id of the group that you want to create a team under.

        :rtype: team
        """
        pass

    def clone_team(self, team_id=None):
        """ Copy the team and its associated group.

        :param team_id: the group_id of the group that you want to create a team under.

        :rtype: teamsAsyncOperation
        """
        pass

    def archive_team(self, team_id=None, readOnlyForMembers=False):
        """ Put the team in a read-only state.

        :param team_id: the group_id of the group that you want to create a team under.

        :rtype: teamsAsyncOperation
        """

        if not team_id:
            raise RuntimeError('Provide the team_id')

        if team_id:
            url = self.build_url(
                self._endpoints.get('archive_team').format(team_id=team_id))

        response = self.con.post(url)

        if not response:
            return None

        if response.status_code == 202:
            data = TeamAsyncOperation.get_request(self, response.headers['Location'])

        else:
            return response.status_code

        return self.team_async_constructor(parent=self, **{self._cloud_data_key: data})

    def unarchive_team(self, team_id=None):
        """ Restore the team to a read-write state.

        :param team_id: the group_id of the group that you want to create a team under.

        :rtype: teamsAsyncOperation
        """
        if not team_id:
            raise RuntimeError('Provide the team_id')

        if team_id:
            url = self.build_url(
                self._endpoints.get('unarchive_team').format(team_id=team_id))

        response = self.con.post(url)

        if not response:
            return None

        if response.status_code == 202:
            data = TeamAsyncOperation.get_request(self, response.headers['Location'])

        else:
            return response.status_code

        return self.team_async_constructor(parent=self, **{self._cloud_data_key: data})

    def install_app(self, team_id=None):
        """ Adds (installs) an app to a team.

        :param team_id: the group_id of the group that you want to create a team under.

        :rtype: teamsAppInstallation
        """
        pass
