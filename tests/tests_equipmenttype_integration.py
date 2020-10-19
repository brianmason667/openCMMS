from django.contrib.auth.models import Permission
from django.test import TestCase
from maintenancemanagement.models import (
    Equipment,
    EquipmentType,
    Field,
    FieldGroup,
    FieldValue,
)
from maintenancemanagement.serializers import (
    EquipmentTypeDetailsSerializer,
    EquipmentTypeSerializer,
)
from openCMMS import settings
from rest_framework.test import APIClient
from usersmanagement.models import UserProfile

User = settings.AUTH_USER_MODEL

#note à la personne faisant passer les tests : il faudra sûrement changer les imports et checker les URL


class EquipmentTypeTests(TestCase):

    def set_up_perm(self):
        """
            Set up a user with permissions
        """
        permission = Permission.objects.get(codename='add_equipmenttype')
        permission2 = Permission.objects.get(codename='view_equipmenttype')
        permission3 = Permission.objects.get(codename='delete_equipmenttype')
        permission4 = Permission.objects.get(codename='change_equipmenttype')
        user = UserProfile.objects.create(username='tom')
        user.set_password('truc')
        user.first_name = 'Tom'
        user.save()
        user.user_permissions.add(permission)
        user.user_permissions.add(permission2)
        user.user_permissions.add(permission3)
        user.user_permissions.add(permission4)
        user.save()
        return user

    def set_up_without_perm(self):
        """
            Set up a user without permissions
        """
        user = UserProfile.objects.create(username='tom')
        user.set_password('truc')
        user.first_name = 'Tom'
        user.save()
        return user

    def test_US4_I9_equipmenttypelist_get_with_perm(self):
        """
            Test if a user with perm receive the data
        """
        self.set_up_perm()
        equipment_type = EquipmentType.objects.all()
        serializer = EquipmentTypeSerializer(equipment_type, many=True)
        client = APIClient()
        user = UserProfile.objects.get(username='tom')
        client.force_authenticate(user=user)
        response = client.get('/api/maintenancemanagement/equipmenttypes/', format='json')
        self.assertEqual(serializer.data, response.json())

    def test_US4_I9_equipmenttypelist_get_without_perm(self):
        """
            Test if a user without perm doesn't receive the data
        """
        self.set_up_without_perm()
        client = APIClient()
        user = UserProfile.objects.get(username='tom')
        client.force_authenticate(user=user)
        response = client.get('/api/maintenancemanagement/equipmenttypes/', format='json')
        self.assertEqual(response.status_code, 401)

    def test_US4_I10_equipmenttypelist_post_with_perm(self):
        """
            Test if a user with perm can add an equipment type
        """
        self.set_up_perm()
        client = APIClient()
        user = UserProfile.objects.get(username='tom')
        client.force_authenticate(user=user)
        response = client.post(
            '/api/maintenancemanagement/equipmenttypes/', {
                'name': 'car',
                'equipment_set': []
            }, format='json'
        )
        self.assertEqual(response.status_code, 201)

    def test_US4_I10_equipmenttypelist_post_without_perm(self):
        """
            Test if a user without perm can't add an equipment type
        """
        self.set_up_without_perm()
        client = APIClient()
        user = UserProfile.objects.get(username='tom')
        client.force_authenticate(user=user)
        response = client.post('/api/maintenancemanagement/equipmenttypes/', {'name': 'tool'}, format='json')
        self.assertEqual(response.status_code, 401)

    def test_US4_I11_equipmenttypedetail_get_with_perm(self):
        """
            Test if a user with perm can see an equipment type detail
        """
        self.set_up_perm()
        tool = EquipmentType.objects.create(name="tool")
        serializer = EquipmentTypeDetailsSerializer(tool)
        client = APIClient()
        user = UserProfile.objects.get(username='tom')
        client.force_authenticate(user=user)
        response = client.get('/api/maintenancemanagement/equipmenttypes/' + str(tool.id) + "/", format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(serializer.data, response.json())

    def test_US4_I11_equipmenttypedetail_get_without_perm(self):
        """
            Test if a user without perm can't see
        """
        self.set_up_without_perm()
        tool = EquipmentType.objects.create(name="tool")
        serializer = EquipmentTypeSerializer(tool)
        client = APIClient()
        user = UserProfile.objects.get(username='tom')
        client.force_authenticate(user=user)
        response = client.get('/api/maintenancemanagement/equipmenttypes/' + str(tool.id) + "/", format='json')
        self.assertEqual(response.status_code, 401)

    def test_US4_I12_equipmenttypedetail_put_with_perm(self):
        """
            Test if a user with perm can change an equipment type detail
        """
        self.set_up_perm()
        tool = EquipmentType.objects.create(name="tool")
        client = APIClient()
        user = UserProfile.objects.get(username='tom')
        client.force_authenticate(user=user)
        response = client.put(
            '/api/maintenancemanagement/equipmenttypes/' + str(tool.id) + '/', {"name": "car"}, format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(EquipmentType.objects.get(name="car"))

    def test_US4_I12_equipmenttypedetail_put_without_perm(self):
        """
            Test if a user without perm can't change an equipment type detail
        """
        self.set_up_without_perm()
        tool = EquipmentType.objects.create(name="tool")
        client = APIClient()
        user = UserProfile.objects.get(username='tom')
        client.force_authenticate(user=user)
        response = client.put(
            '/api/maintenancemanagement/equipmenttypes/' + str(tool.id) + '/', {"name": "car"}, format='json'
        )
        self.assertEqual(response.status_code, 401)

    def test_US4_I13_equipmenttypedetail_delete_with_perm(self):
        """
            Test if a user with perm can delete an equipment type
        """
        self.set_up_perm()
        user = UserProfile.objects.get(username="tom")
        client = APIClient()
        client.force_authenticate(user=user)
        tool = EquipmentType.objects.create(name="tool")
        response_1 = client.get('/api/maintenancemanagement/equipmenttypes/' + str(tool.id) + '/', format='json')
        response_2 = client.delete('/api/maintenancemanagement/equipmenttypes/' + str(tool.id) + '/')
        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_2.status_code, 204)
        self.assertFalse(EquipmentType.objects.filter(id=tool.id).exists())

    def test_US4_I13_equipmenttypedetail_delete_without_perm(self):
        """
            Test if a user without perm can't deletean equipment type
        """
        self.set_up_perm()
        user = UserProfile.objects.get(username="tom")
        client = APIClient()
        client.force_authenticate(user=user)
        tool = EquipmentType.objects.create(name="tool")
        response_1 = client.get('/api/maintenancemanagement/equipmenttypes/' + str(tool.id) + '/', format='json')
        response_2 = client.delete('/api/maintenancemanagement/equipmenttypes/' + str(tool.id) + '/')
        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_2.status_code, 204)
        self.assertFalse(EquipmentType.objects.filter(id=tool.id).exists())

    def test_US20_I1_equipmenttypelist_post_with_fields_with_perm(self):
        """
            Test if a user with perm can add an equipment type with fields
        """
        self.set_up_perm()
        client = APIClient()
        user = UserProfile.objects.get(username='tom')
        client.force_authenticate(user=user)
        response = client.post(
            '/api/maintenancemanagement/equipmenttypes/', {
                'name':
                    'car',
                'equipment_set': [],
                'field':
                    [
                        {
                            "name": "test_add_equipmenttype_with_perm_with_fields_1"
                        }, {
                            "name": "test_add_equipmenttype_with_perm_with_fields_2",
                            "value": ["Renault", "Volvo", "BMW"]
                        }
                    ]
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        equipment_type = EquipmentType.objects.get(name="car")
        field_group = FieldGroup.objects.get(name="car")
        field_1 = Field.objects.get(name="test_add_equipmenttype_with_perm_with_fields_1")
        field_2 = Field.objects.get(name="test_add_equipmenttype_with_perm_with_fields_2")
        field_value_1 = FieldValue.objects.get(value="Renault")
        field_value_2 = FieldValue.objects.get(value="Volvo")
        field_value_3 = FieldValue.objects.get(value="BMW")
        self.assertEqual(field_1.field_group, field_group)
        self.assertEqual(field_2.field_group, field_group)
        self.assertTrue(equipment_type in field_group.equipmentType_set.all())
        self.assertEqual(field_value_1.field, field_2)
        self.assertEqual(field_value_2.field, field_2)
        self.assertEqual(field_value_3.field, field_2)