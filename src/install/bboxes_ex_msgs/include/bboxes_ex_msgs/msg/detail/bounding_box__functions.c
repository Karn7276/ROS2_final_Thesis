// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from bboxes_ex_msgs:msg/BoundingBox.idl
// generated code does not contain a copyright notice
#include "bboxes_ex_msgs/msg/detail/bounding_box__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `class_id`
#include "rosidl_runtime_c/string_functions.h"

bool
bboxes_ex_msgs__msg__BoundingBox__init(bboxes_ex_msgs__msg__BoundingBox * msg)
{
  if (!msg) {
    return false;
  }
  // probability
  // xmin
  // ymin
  // xmax
  // ymax
  // id
  // img_width
  // img_height
  // center_dist
  // class_id
  if (!rosidl_runtime_c__String__init(&msg->class_id)) {
    bboxes_ex_msgs__msg__BoundingBox__fini(msg);
    return false;
  }
  // class_id_int
  return true;
}

void
bboxes_ex_msgs__msg__BoundingBox__fini(bboxes_ex_msgs__msg__BoundingBox * msg)
{
  if (!msg) {
    return;
  }
  // probability
  // xmin
  // ymin
  // xmax
  // ymax
  // id
  // img_width
  // img_height
  // center_dist
  // class_id
  rosidl_runtime_c__String__fini(&msg->class_id);
  // class_id_int
}

bboxes_ex_msgs__msg__BoundingBox *
bboxes_ex_msgs__msg__BoundingBox__create()
{
  bboxes_ex_msgs__msg__BoundingBox * msg = (bboxes_ex_msgs__msg__BoundingBox *)malloc(sizeof(bboxes_ex_msgs__msg__BoundingBox));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(bboxes_ex_msgs__msg__BoundingBox));
  bool success = bboxes_ex_msgs__msg__BoundingBox__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
bboxes_ex_msgs__msg__BoundingBox__destroy(bboxes_ex_msgs__msg__BoundingBox * msg)
{
  if (msg) {
    bboxes_ex_msgs__msg__BoundingBox__fini(msg);
  }
  free(msg);
}


bool
bboxes_ex_msgs__msg__BoundingBox__Sequence__init(bboxes_ex_msgs__msg__BoundingBox__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  bboxes_ex_msgs__msg__BoundingBox * data = NULL;
  if (size) {
    data = (bboxes_ex_msgs__msg__BoundingBox *)calloc(size, sizeof(bboxes_ex_msgs__msg__BoundingBox));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = bboxes_ex_msgs__msg__BoundingBox__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        bboxes_ex_msgs__msg__BoundingBox__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
bboxes_ex_msgs__msg__BoundingBox__Sequence__fini(bboxes_ex_msgs__msg__BoundingBox__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      bboxes_ex_msgs__msg__BoundingBox__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

bboxes_ex_msgs__msg__BoundingBox__Sequence *
bboxes_ex_msgs__msg__BoundingBox__Sequence__create(size_t size)
{
  bboxes_ex_msgs__msg__BoundingBox__Sequence * array = (bboxes_ex_msgs__msg__BoundingBox__Sequence *)malloc(sizeof(bboxes_ex_msgs__msg__BoundingBox__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = bboxes_ex_msgs__msg__BoundingBox__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
bboxes_ex_msgs__msg__BoundingBox__Sequence__destroy(bboxes_ex_msgs__msg__BoundingBox__Sequence * array)
{
  if (array) {
    bboxes_ex_msgs__msg__BoundingBox__Sequence__fini(array);
  }
  free(array);
}
