from rest_framework import serializers
from .models import Employee, AddressDetails, WorkExperience, Qualification, Project

class AddressDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressDetails
        fields = '__all__'

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    address_details = AddressDetailsSerializer()
    work_experience = WorkExperienceSerializer(many=True)
    qualifications = QualificationSerializer(many=True)
    projects = ProjectSerializer(many=True)

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        address_data = validated_data.pop('address_details')
        print("address",address_data)
        address = AddressDetails.objects.create(**address_data)
        
        work_experiences_data = validated_data.pop('work_experience')
        qualifications_data = validated_data.pop('qualifications')
        projects_data = validated_data.pop('projects')
        
        employee = Employee.objects.create(address_details=address, **validated_data)
        
        for we_data in work_experiences_data:
            we = WorkExperience.objects.create(**we_data)
            employee.work_experience.add(we)
        
        for q_data in qualifications_data:
            q = Qualification.objects.create(**q_data)
            employee.qualifications.add(q)
        
        for p_data in projects_data:
            p = Project.objects.create(**p_data)
            employee.projects.add(p)
        
        return employee

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address_details')
        AddressDetails.objects.filter(id=instance.address_details.id).update(**address_data)
        
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.phone_no = validated_data.get('phone_no', instance.phone_no)
        
        instance.save()

        # Update work experiences
        work_experiences_data = validated_data.pop('work_experience')
        instance.work_experience.clear()
        for we_data in work_experiences_data:
            we = WorkExperience.objects.create(**we_data)
            instance.work_experience.add(we)

        # Update qualifications
        qualifications_data = validated_data.pop('qualifications')
        instance.qualifications.clear()
        for q_data in qualifications_data:
            q = Qualification.objects.create(**q_data)
            instance.qualifications.add(q)

        # Update projects
        projects_data = validated_data.pop('projects')
        instance.projects.clear()
        for p_data in projects_data:
            p = Project.objects.create(**p_data)
            instance.projects.add(p)
        
        return instance


    